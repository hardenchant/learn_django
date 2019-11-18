# Generated by Django 2.2.4 on 2019-11-16 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20191116_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='knowledge',
            field=models.ManyToManyField(blank=True, help_text='Курсы, которые Вы можете преподавать', related_name='Profile_knowledge', to='core.Course'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='studying',
            field=models.ManyToManyField(blank=True, help_text='Курсы, которые Вы уже изучаете', related_name='Profile_studying', to='core.Course'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='teaching',
            field=models.ManyToManyField(blank=True, help_text='Курсы, которые Вы уже преподаёте', related_name='Profile_teaching', to='core.Course'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='wishes',
            field=models.ManyToManyField(blank=True, help_text='Курсы, которые Вы хотите изучать', related_name='Profile_wishes', to='core.Course'),
        ),
    ]