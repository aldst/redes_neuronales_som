from django import forms
from .models import *


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['edad','imc','hemog','hemog_ajustada']

        widget = {
            'edad': forms.IntegerField(min_value=0),
            'imc': forms.FloatField(min_value=12, max_value=100),
            'hemog': forms.FloatField(min_value=4, max_value=21),
            'hemog_ajustada': forms.FloatField(min_value=4, max_value=21)
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class': "form-control"
                }
            )