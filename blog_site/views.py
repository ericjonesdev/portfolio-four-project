from django.shortcuts import render


def get_homepage(request):
    return render(request, 'blog_site/blog_site_list.html')
