from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, ListView, CreateView
import matplotlib.pyplot as plt
import os
import numpy as np
from django.template import Template, Context


# Create your views here.


class SOM:
    data = out = weight = None

    def __init__(self, dim, rows, col, factor, itera):
        self.dimension = dim
        self.rows = rows
        self.cols = col
        self.learning_factor = factor
        self.iterations = itera

    def training_Data(self, file):
        file = os.path.realpath(file)
        self.data = np.loadtxt(file, delimiter=",",
                               usecols=range(0, self.dimension),
                               dtype=np.float64)
        self.out = np.loadtxt(file, delimiter=",", usecols=[self.dimension],
                              dtype=np.float64)
        self.weight = np.random.randn(self.rows, self.cols, self.dimension)

    def learning_algorithm(self, dato):

        def BMU(pattern):
            result = (0, 0)
            shortest_distance = 1.0e20

            for row in range(self.rows):
                for col in range(self.cols):
                    dist = np.linalg.norm(
                        self.weight[row][col] - self.data[pattern])
                    if dist < shortest_distance:
                        shortest_distance = dist
                        result = (row, col)

            return result

        def BMU_DATA(dato):
            result = (0, 0)
            shortest_distance = 1.0e20

            for row in range(self.rows):
                for col in range(self.cols):
                    dist = np.linalg.norm(self.weight[row][col] - dato)
                    if dist < shortest_distance:
                        shortest_distance = dist
                        result = (row, col)

            return result

        def manhattan_distance(r1, c1, r2, c2):
            return np.abs(r1 - r2) + np.abs(c1 - c2)

        def most_common(lst, n):
            if len(lst) == 0: return -1
            counts = np.zeros(shape=n, dtype=np.int)
            for i in range(len(lst)):
                counts[int(lst[i])] += 1
            return np.argmax(counts)

        def find_result(mapa, Rows, Cols, bmu_row_data, bmu_col_data):
            salida = None
            delta_aumento = 1
            x = bmu_row_data
            y = bmu_col_data
            while salida is None or delta_aumento < Rows + 2:
                for i in range(delta_aumento):
                    for j in range(delta_aumento):
                        if Rows > x + i >= 0 and Cols > y + j >= 0:
                            if len(mapa[x + i][y + j]) > 0:
                                salida = mapa[x + i][y + j][0]
                                print("salida")
                                return int(salida)

                x -= 1
                y -= 1
                delta_aumento += 2
            return salida

        def display_result(dato):

            print("entrada:", dato)
            (bmu_row_data, bmu_col_data) = BMU_DATA(dato)

            maps = np.empty(shape=(self.rows, self.cols), dtype=object)

            for row in range(self.rows):
                for col in range(self.cols):
                    maps[row][col] = []

            for pattern in range(len(self.data)):
                (row, col) = BMU(pattern)
                maps[row][col].append(self.out[pattern])

            label_pesos = np.zeros(shape=(self.rows, self.cols), dtype=np.int)
            for i in range(self.rows):
                for j in range(self.cols):
                    label_pesos[i][j] = most_common(maps[i][j], 20)
            plt.imshow(label_pesos)
            plt.colorbar()
            plt.savefig("test.png")
            return find_result(maps, self.rows, self.cols, bmu_row_data,
                               bmu_col_data)

        max_range = self.rows + self.cols

        for itera in range(self.iterations):
            alfa = 1.0 - (itera * 1.0) / self.iterations
            alfaActual = alfa * self.learning_factor
            neighbors = (int)(alfa * max_range)

            learning_pattern = np.random.randint(len(self.data))
            (bmu_row, bmu_col) = BMU(learning_pattern)

            for col in range(self.cols):
                for fil in range(self.rows):
                    if manhattan_distance(bmu_row, bmu_col, col,
                                          fil) < neighbors:
                        self.weight[col][fil] += alfaActual * (
                                self.data[learning_pattern] -
                                self.weight[col][fil])

        return display_result(dato)


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

"""
def DiagnosticPatient(request, ListView):
    model = Patient
    template_name = 'som/patient_diagnostic.html'
    form_class = PatientForm
    success_url = reverse_lazy('som:list_patient')
"""

def execute(dato):
    np.random.seed(1)
    som = SOM(13, 60, 60, 0.2, 1500)
    som.training_Data(".../static/texto/cardiaca.txt")
    return som.learning_algorithm(dato)


def diagnostic(request, id):
    patient = Patient.objects.get(id=id)
    data = [float(patient.age), float(patient.sex), float(patient.cp),
            float(patient.trestbps), float(patient.chol),
            float(patient.fbs), float(patient.restecg), float(patient.thalach),
            float(patient.exang),
            float(patient.oldpeak), float(patient.slope), float(patient.ca),
            float(patient.thal)]

    result = execute(data)
    response = str(result)
    print(response)

    return render(request, 'som/patient_diagnostic.html', {'response': response})
