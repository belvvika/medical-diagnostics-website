from django.forms import ModelForm

from website.models import PatientContacts
class PatientForm(ModelForm):
    class Meta:
        model = PatientContacts
        fields = ['phone_number', 'first_name']

