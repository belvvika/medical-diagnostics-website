from django.urls import path
from website.views import base, MedicalServicesListView, PatientContactsListView, PatientContactsCreateView, CompanyListView, DoctorsListView

app_name = 'website'

urlpatterns = [
    path('', base),

    path('website/medicalservices_list', MedicalServicesListView.as_view(), name='medicalservices_list'),

    path('website/patientcontacts_list', PatientContactsListView.as_view(), name='patientcontacts_list'),
    path('website/patientcontacts_create', PatientContactsCreateView.as_view(), name='patientcontacts_create'),

    path('website/company_list', CompanyListView.as_view(), name='company_list'),

    path('website/doctors_list', DoctorsListView.as_view(), name='doctors_list'),

]
