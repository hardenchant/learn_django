# Generated by Django 2.2.4 on 2019-08-29 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_news'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='title',
        ),
        migrations.AddField(
            model_name='news',
            name='headline',
            field=models.CharField(default='Внимание!', help_text='Заголовок', max_length=100, verbose_name='Основная суть, объявление'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(auto_now=True, help_text='Время объявления'),
        ),
        migrations.AlterField(
            model_name='news',
            name='message',
            field=models.TextField(blank=True, help_text='Сама новость', max_length=5000, null=True),
        ),
    ]