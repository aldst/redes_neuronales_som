from django.contrib import admin
from .models import *


class PatientAdmin(admin.ModelAdmin):
    list_display = (
        'age','sex','cp','trestbps','chol','fbs','restecg',
        'thalach','exang','oldpeak','slope','ca','thal',
    )

    ordering = ('id',)


admin.site.register(Patient, PatientAdmin)
