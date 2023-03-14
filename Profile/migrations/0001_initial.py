# Generated by Django 4.1.5 on 2023-03-08 17:00

import Profile.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Дата Рождения')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=Profile.models.get_name_photo_file, verbose_name='Фото')),
                ('rating', models.FloatField(default=0.0, max_length=5.0, verbose_name='Рейтинг')),
            ],
            options={
                'verbose_name': 'Информация о пользователе',
                'verbose_name_plural': 'Информация о пользователях',
            },
        ),
    ]
