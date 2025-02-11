from django.db import models


class PersonData(models.Model):
    GENDER_CHOICES = (
        ('male', 'Мужской'),
        ('female', 'Женский'),
        ('prefer_not_to_say', 'Предпочитаю не говорить')
    )

    image = models.ImageField(upload_to='images/', verbose_name="Фото", blank=True, null=True)
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия")
    hobby = models.TextField(verbose_name="Хобби")
    gender = models.CharField(max_length=255, verbose_name="Пол", choices=GENDER_CHOICES)
    nationality = models.CharField(max_length=255, verbose_name="Национальность", blank=True, null=True)
    height = models.FloatField(verbose_name="Рост")
    weight = models.FloatField(verbose_name="Вес")
    skin_color = models.CharField(max_length=255, verbose_name="Цвет кожи")
    email = models.EmailField(verbose_name="Электронная почта",)
    phone = models.CharField(max_length=255, verbose_name="Телефон")
    address = models.CharField(max_length=255, verbose_name="Адрес", blank=True, null=True)
    date_of_birth = models.DateField(verbose_name="Дата рождения")
