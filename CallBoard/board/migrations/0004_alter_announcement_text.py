# Generated by Django 4.2.7 on 2023-12-02 15:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('board', '0003_alter_announcement_text_alter_announcement_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='text',
            field=models.CharField(max_length=255, verbose_name='Содержание'),
        ),
    ]