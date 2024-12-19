# Generated by Django 5.1.4 on 2024-12-18 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_doctor', models.CharField(help_text='Укажите имя врача', max_length=100, verbose_name='Имя врача')),
                ('specialization', models.CharField(help_text='Укажите специализацию врача', max_length=100, verbose_name='Специализация врача')),
                ('work_experience', models.PositiveIntegerField(help_text='Укажите стаж работы врача', verbose_name='Стаж работы врача')),
            ],
            options={
                'verbose_name': 'Врач',
                'verbose_name_plural': 'Врачи',
            },
        ),
    ]
