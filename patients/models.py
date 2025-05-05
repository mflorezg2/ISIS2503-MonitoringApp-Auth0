from django.db import models

class Paciente(models.Model):
    name               = models.CharField("Nombre", max_length=100)
    birth_date         = models.DateField("Fecha de nacimiento")
    age                = models.PositiveIntegerField("Edad")
    gender             = models.CharField("Sexo", max_length=10)
    blood_type         = models.CharField("Tipo de sangre", max_length=3)
    allergies          = models.TextField("Alergias", blank=True)
    medical_conditions = models.TextField("Condiciones médicas", blank=True)

    def __str__(self):
        return self.name

