# Generated by Django 4.2.7 on 2023-12-09 07:16

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OneTimeCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255, verbose_name='Пользователь')),
                ('code', models.CharField(max_length=6, verbose_name='Код')),
            ],
        ),
    ]