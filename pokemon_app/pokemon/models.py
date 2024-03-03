from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Pokemon(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    name = models.CharField(max_length=255, verbose_name='Имя', blank=True, null=True)
    portrait = models.ImageField(upload_to='portrait/', null=True, verbose_name='Портрет', blank=True)

    experience = models.IntegerField(verbose_name='Опыт', blank=True, null=True)
    level = models.IntegerField(verbose_name='Уровень', blank=True, null=True)

    hp = models.IntegerField(verbose_name='Здоровье', blank=True, null=True)

    strength = models.IntegerField(verbose_name='Сила', blank=True, null=True)
    constitution = models.IntegerField(verbose_name='Телосложение', blank=True, null=True)

    win_count = models.IntegerField(verbose_name='Количество побед', blank=True, null=True)
    defeat_count = models.IntegerField(verbose_name='Количество поражений', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Покемон'
        verbose_name_plural = 'Покемоны'
        ordering = ['id']