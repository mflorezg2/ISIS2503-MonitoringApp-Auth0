from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['name','birth_date','age','gender','blood_type','allergies','medical_conditions']
