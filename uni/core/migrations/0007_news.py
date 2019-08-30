# Generated by Django 2.2.4 on 2019-08-25 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190810_0857'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now=True)),
                ('message', models.TextField(max_length=5000)),
            ],
        ),
    ]
