from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.views.generic.edit import DeleteView
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, UserProfiile
from .forms import CommentForm, UserProfileForm
from django.views.generic import DetailView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

User = get_user_model()


class UserProfileView(DetailView):
    model = User
    template_name = 'user_profile.html'
    context_object_name = 'user'
    slug_field = 'username'
    slug_url_kwarg = 'username'


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )


class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class UserProfiileDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = User
    template_name = 'user_profile.html'
    slug_field = 'username'

    def test_func(self):
        user = self.get_object()
        return self.request.user == user

    def get_object(self, queryset=None):
        return get_object_or_404(User, username=self.kwargs['username'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profiile = get_object_or_404(UserProfiile, user=self.object)
        context['profile'] = user_profiile
        return context


class UserProfiileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserProfiile
    template_name = 'update_profile.html'
    fields = ['profile_image', 'first_name', 'last_name', 'bio', 'dob', 'location', 'github', 'website', 'twitter', 'occupation']
    success_url = '/'
    
    def test_func(self):
        return self.get_object().user == self.request.user

    def get_object(self, queryset=None):
        obj, created = UserProfiile.objects.get_or_create(user=self.request.user)
        return obj
   

class UserProfiileDeleteView(LoginRequiredMixin, DeleteView):
    model = UserProfiile
    success_url = reverse_lazy('home')
    template_name = 'userprofile_confirm_delete.html'

    def get_object(self, queryset=None):
        obj = get_object_or_404(UserProfile, user=self.request.user)
        return obj
