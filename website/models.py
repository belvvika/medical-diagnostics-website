from django.db import models


class MedicalServices(models.Model):
    name_services = models.CharField(
        max_length=200,
        verbose_name='Название медицинской услуги',
        help_text='Укажите название медицинской услуги'
    )
    description = models.TextField(
        verbose_name='Описание медицинской услуги',
        help_text='Введите описание медицинской услуги'
    )
    price = models.DecimalField(
        verbose_name='Цена медицинской услуги',
        max_digits=10,
        decimal_places=2,
        help_text='Укажите цену медицинской услуги'
    )

    class Meta:
        verbose_name = 'Медицинская услуга'
        verbose_name_plural = 'Медицинские услуги'

class PatientContacts(models.Model):
    phone_number = models.CharField(
        max_length=20,
        verbose_name='Номер телефона пациента',
        help_text='Укажите номер телефона пациента'
    )
    first_name = models.CharField(
        max_length=30,
        verbose_name='Имя пациента',
        help_text='Укажите имя пациента'
    )

    class Meta:
        verbose_name = 'Контакты пациента'

class Company(models.Model):
    name_company = models.CharField(
        max_length=200,
        verbose_name='Название компании',
        help_text='Укажите название компании'
    )
    description = models.TextField(
        verbose_name='Описание компании',
        help_text='Введите описание компании'
    )
    address = models.CharField(
        max_length=100,
        verbose_name='Адрес',
        help_text='Укажите адрес компании'
    )
    phone_number = models.CharField(
        max_length=20,
        verbose_name='Номер телефона',
        help_text='Укажите номер телефона компании'
    )
    email = models.EmailField(
        verbose_name='Электронная почта',
        help_text='Укажите электронную почту компании'
    )

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

class Doctors(models.Model):
    name_doctor = models.CharField(
        max_length=100,
        verbose_name='Имя врача',
        help_text='Укажите имя врача'
    )
    specialization = models.CharField(
        max_length=100,
        verbose_name='Специализация врача',
        help_text='Укажите специализацию врача'
    )
    work_experience = models.PositiveIntegerField(
        verbose_name='Стаж работы врача',
        help_text='Укажите стаж работы врача'
    )

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'
