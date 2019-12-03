# Generated by Django 2.2.4 on 2019-11-22 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0012_auto_20191122_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='teacher',
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(blank=True, help_text='Преподаватель курса', null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
