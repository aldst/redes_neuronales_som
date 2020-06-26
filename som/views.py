from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, ListView, CreateView

# Create your views here.


class ListPatient(ListView):
    model = Patient
    template_name = 'som/patient.html'


class CreatePatient(SuccessMessageMixin, CreateView):
    model = Patient
    template_name = 'som/patient_form.html'
    form_class = PatientForm
    success_url = reverse_lazy('som:list_patient')
    success_message = "Paciente creado satisfactoriamente"


class EditPatient(SuccessMessageMixin, UpdateView):
    model = Patient
    template_name = 'som/patient_form.html'
    form_class = PatientForm
    success_url = reverse_lazy('som:list_patient')
    success_message = "Paciente editado satisfactoriamente"


class DiagnosticPatient(SuccessMessageMixin, UpdateView):
    model = Patient
    template_name = 'som/patient_diagnostic.html'
