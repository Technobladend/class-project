from django.apps import AppConfig


class PersonalMatterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.v1.personal_matter'
    verbose_name = 'Личные данные'
    verbose_name_plural = 'Личные данные'
