from django.db import models

from pokemon.models import Pokemon


class Arena(models.Model):
    owner_pokemon = models.ForeignKey(to=Pokemon, on_delete=models.CASCADE, related_name='Покемон', null=True,
                                      blank=True)
    enemy_pokemon = models.ForeignKey(to=Pokemon, on_delete=models.CASCADE, related_name='Противник', null=True,
                                      blank=True)
    result = models.CharField(max_length=255, verbose_name='Результат', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Арена'
        verbose_name_plural = 'Арена'
        ordering = ['id']

    def __str__(self):
        return f'{self.owner_pokemon} - {self.enemy_pokemon}'


class Log(models.Model):
    battle = models.ForeignKey(to=Arena, on_delete=models.CASCADE, related_name='battle', null=True,
                               blank=True)
    action = models.CharField(max_length=255, verbose_name='Действие', blank=True, null=True)
    winner = models.CharField(max_length=255, verbose_name='Победитель', blank=True, null=True)

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Лог'
        ordering = ['id']

    def __str__(self):
        return f'{self.battle}'