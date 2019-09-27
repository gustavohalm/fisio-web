from django.shortcuts import render, redirect
from api import models
from . import forms
# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView


def loginView():
    pass


def logoutView():
    pass


class AppointmentList(ListView):
    template_name = 'painel/list_appointment.html'

    def get_queryset(self):
        return models.Appointment.objects.filter(fisio=self.request.user)


class AppointmentDetail(DetailView):
    model = models.Appointment
    template_name = 'painel/detail_appointment.html'


class AppointmentCreate(CreateView):
    template_name = 'painel/create_appointment.html'
    form_class = forms.AppointmentForm
    model = models.Appointment
    exclude = ['id', 'fisio']

    def post(self, request, *args, **kwargs):
        form = forms.AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            appointment.fisio = self.request.user
            appointment.save()

        return redirect("/consultas")


class PatientList(ListView):
    template_name = 'painel/list_patient.html'

    def get_queryset(self):
        return models.Patient.objects.filter(fisio=self.request.user)


class PatientDetail(DetailView):
    model = models.Patient
    template_name = 'painel/detail_patient.html'


class PatientCreate(CreateView):
    template_name = 'painel/create_patient.html'
    form_class = forms.PatientForm
    model = models.Patient

    exclude = ['id', 'fisio']

    def post(self, request, *args, **kwargs):
        form = forms.PatientForm(request.POST)
        if form.is_valid():
            patient = form.save()
            patient.fisio = self.request.user
            patient.save()
        return redirect('/pacientes')
