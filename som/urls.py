from django.urls import path
from .views import *

app_name = 'som'

urlpatterns = [
    path('', ListPatient.as_view(), name='list_patient'),
    path('patient/register/', CreatePatient.as_view(), name='register_patient'),
    path('patient/edit/<int:pk>', EditPatient.as_view(), name='edit_patient'),
]


