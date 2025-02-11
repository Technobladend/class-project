from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.v1.home'
    verbose_name = 'Главная страница'
    verbose_name_plural = 'Главная страница'