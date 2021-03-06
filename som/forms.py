from django import forms
from .models import *


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

        widget = {
            'age': forms.IntegerField(min_value=0),
            'sex': forms.IntegerField(),
            'cp': forms.IntegerField(),
            'trestbps': forms.IntegerField(min_value=0),
            'chol': forms.IntegerField(min_value=0),
            'fbs': forms.IntegerField(),
            'restecg': forms.IntegerField(),
            'thalach': forms.IntegerField(min_value=0),
            'exang': forms.IntegerField(),
            'oldpeak': forms.IntegerField(min_value=0),
            'slope': forms.IntegerField(),
            'ca': forms.IntegerField(),
            'thal': forms.IntegerField()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class': "form-control"
                }
            )
