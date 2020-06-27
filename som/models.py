from django.db import models

# Create your models here.

class Patient(models.Model):

    CHOICE_SEX = (
        (0,('MASCULINO')),
        (1, ('FEMENINO'))
    )
    CHOICE_CP = (
        (1, 'Angina típica'),
        (2, 'Angina atípica'),
        (3,'Sin dolor de angina'),
        (4,'asintomático')
    )
    CHOICE_FBS = (
        (0, 'VERDADERO'),
        (1, 'FALSO')
    )
    CHOICE_RESTECG = (
        (0, 'normal'),
        (1, 'anormal'),
        (2, 'probable hipertrofia ventricular')
    )
    CHOICE_SLOPE = (
        (1, 'bajo'),
        (2, 'medio'),
        (3, 'alto')
    )
    CHOICE_THAL = (
        (3, 'normal'),
        (6, 'defecto solucionable'),
        (7, 'defecto reversible')
    )
    CHOICE_EXANG = (
        (0, 'no'),
        (1, 'si')
    )
    CHOICE_CA = (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3)
    )

    age = models.PositiveSmallIntegerField("Edad")
    sex = models.IntegerField("Sexo",choices=CHOICE_SEX)
    cp = models.IntegerField("Dolor de pecho",choices=CHOICE_CP)
    trestbps = models.PositiveIntegerField("Presión de sangre")
    chol = models.PositiveIntegerField("Colesterol")

    fbs = models.IntegerField("Nivel de azúcar en ayuno",choices=CHOICE_FBS)
    
    restecg = models.IntegerField("Res. electrocardiográficos",choices=CHOICE_RESTECG)
    thalach = models.PositiveIntegerField("Nivel maximo de frecuencia cardiaca")
    exang = models.IntegerField("Angila inducida por ejercicio",choices=CHOICE_EXANG)
    oldpeak = models.PositiveIntegerField("Depresión ST inducida")
    slope = models.IntegerField("Pico más alto",choices=CHOICE_SLOPE)
    ca = models.IntegerField("Núm vasos principales",choices=CHOICE_CA)
    thal = models.IntegerField("thal",choices=CHOICE_THAL)
    result = models.IntegerField("Resultado", null=True, blank=True)

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        db_table = "pacientes"

    def __str__(self):
        return f"{self.age} - {self.sex} - {self.cp} - {self.trestbps} - {self.chol} - {self.fbs} - {self.restecg} - {self.thalach} - {self.exang} - {self.oldpeak} - {self.slope} - {self.ca} - {self.thal} - {self.result}"
