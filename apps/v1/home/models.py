from django.db import models

class Wise_quotes(models.Model):
    quote = models.CharField(max_length=255, unique=True,  verbose_name="Цитата")
    author = models.CharField(max_length=255, verbose_name="Автор")

    def __str__(self):
        return self.quote

    class Meta:
        verbose_name = 'Цитата'
        verbose_name_plural = 'Цитаты'


class HeaderModel(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Шапка страницы'
        verbose_name_plural = 'Шапка страницы'


class FooterModel(models.Model):
    address = models.CharField(max_length=255, verbose_name="Адрес")

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Подвал Страницы'
        verbose_name_plural = 'Подвал Страницы'


