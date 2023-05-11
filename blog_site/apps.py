from django.apps import AppConfig


class BlogSiteConfig(AppConfig):
    '''
    defines the configuration for the 'blog_site' Django app, including the
    default auto field and the app name.
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog_site'
