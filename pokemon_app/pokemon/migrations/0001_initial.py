# Generated by Django 4.2.3 on 2024-03-02 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя')),
                ('portrait', models.ImageField(blank=True, null=True, upload_to='portrait/', verbose_name='Портрет')),
                ('experience', models.IntegerField(blank=True, null=True, verbose_name='Опыт')),
                ('hp', models.IntegerField(blank=True, null=True, verbose_name='Здоровье')),
                ('ac', models.IntegerField(blank=True, null=True, verbose_name='Класс доспехов')),
                ('strength', models.IntegerField(blank=True, null=True, verbose_name='Сила')),
                ('dexterity', models.IntegerField(blank=True, null=True, verbose_name='Ловкость')),
                ('constitution', models.IntegerField(blank=True, null=True, verbose_name='Телосложение')),
                ('win_count', models.IntegerField(blank=True, null=True, verbose_name='Количество побед')),
                ('defeat_count', models.IntegerField(blank=True, null=True, verbose_name='Количество поражений')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Покемон',
                'verbose_name_plural': 'Покемоны',
                'ordering': ['id'],
            },
        ),
    ]
