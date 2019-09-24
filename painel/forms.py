from django import forms
from api import  models


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = models.Appointment
        exclude = ['id', 'fisio']


class PatientForm(forms.ModelForm):
    class Meta:
        model = models.Patient
        exclude = ['id', 'fisio']


