# Generated by Django 2.2.4 on 2019-08-10 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_course_date_of_starting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='date_of_starting',
        ),
    ]