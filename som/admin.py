from django.contrib import admin
from .models import *


class PatientAdmin(admin.ModelAdmin):
    list_display = (
        'edad','imc','hemog','hemog_ajustada',
    )

    ordering = ('id',)


admin.site.register(Patient, PatientAdmin)
