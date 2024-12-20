from django.shortcuts import render
from django.urls import reverse_lazy

from website.models import MedicalServices, PatientContacts, Company, Doctors
from website.forms import PatientForm

from django.views.generic import ListView, CreateView


def base(request):
    return render(request, 'website/base.html')

class MedicalServicesListView(ListView):
    model = MedicalServices


class PatientContactsListView(ListView):
    model = PatientContacts

class PatientContactsCreateView(CreateView):
    model = PatientContacts
    form_class = PatientForm
    success_url = reverse_lazy('website:patientcontacts_list')

class CompanyListView(ListView):
    model = Company

class DoctorsListView(ListView):
    model = Doctors

