from django import forms
from .models import *

class Formularios(forms.ModelForm):
    class Meta:
        model = PrescricaoDeEnfermagem
        #model = Leito
        exclude= []

class FormPaciente(forms.ModelForm):
    class Meta:
        model = Paciente
        #model = Leito
        exclude= []
