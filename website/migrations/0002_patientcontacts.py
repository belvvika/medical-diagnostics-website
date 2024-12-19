# Generated by Django 5.1.4 on 2024-12-18 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientContacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(help_text='Укажите номер телефона пациента', max_length=20, verbose_name='Номер телефона пациента')),
                ('first_name', models.CharField(help_text='Укажите имя пациента', max_length=30, verbose_name='Имя пациента')),
            ],
            options={
                'verbose_name': 'Контакты пациента',
            },
        ),
    ]