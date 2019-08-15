# Generated by Django 2.2.4 on 2019-08-10 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group_president',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Староста не найден(а)', help_text='Ответственный за курс', max_length=128, verbose_name='Староста курса')),
                ('telephone', models.CharField(default='Староста не найден(а)', help_text='Номер для связи', max_length=64, verbose_name='Номер телефона')),
                ('vk_id', models.CharField(blank=True, help_text='вк дл связи', max_length=64, null=True, verbose_name='Vk.id')),
                ('email', models.CharField(blank=True, help_text='Адрес электронной почты для связи', max_length=64, null=True, verbose_name='email adress')),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='contact',
            field=models.CharField(default='Место проведения  не найдено', help_text='Контакты для связи', max_length=256, verbose_name='Телефон, vk или telegram'),
        ),
        migrations.AddField(
            model_name='location',
            name='name',
            field=models.CharField(default='Место проведения  не найдено', help_text='Те, кто предоставили место проведения', max_length=256, verbose_name='Название организации или имя владельца помещения'),
        ),
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('done', 'Запущен'), ('in_progress', 'В процессе'), ('teachers', 'Поиск преподавателя'), ('place', 'Поиск места проведения'), ('te_and_pl', 'Поиск места проведения и преподавателя'), ('president', 'Выборы старосты'), ('students', 'Набор людей')], max_length=16),
        ),
        migrations.AlterField(
            model_name='location',
            name='address',
            field=models.CharField(default='Место проведения  не найдено', help_text='Место проведения', max_length=256, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='course',
            name='group_president',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Group_president'),
        ),
    ]