from django.db import models

# Create your models here.


class Patient(models.Model):
    edad = models.IntegerField("Edad")
    imc = models.FloatField("IMC")
    hemog = models.FloatField("Hemoglobina")
    hemog_ajustada = models.FloatField("Hemoglobina Ajustada")

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        db_table = "pacientes"

    def __str__(self):
        return f"{self.edad} - {self.imc} - {self.hemog} - {self.hemog_ajustada}"