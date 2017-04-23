from __future__ import unicode_literals
from django.db import models

# Create your models here

class Paciente(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField()

    #data_nascimento = models.DateField()

def __str__(self):
    return '{}'.format(self.nome)

HORARIOS = (
    (1,"Manhã"),(2, "Tarde"),(3, "Noite")
)
class PrescricaoDeEnfermagem(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    numleito= models.IntegerField()
    turno = models.IntegerField(choices = HORARIOS)
    #leito = models.ForeignKey(Leito, on_delete=models.CASCADE)

class Monitoramento(models.Model):
    prescricaodeenfermagem = models.ForeignKey(PrescricaoDeEnfermagem, on_delete=models.CASCADE)
    #prescricaodeenfermag = models.CharField(max_length=200)

TIPOS_CONTROLE_ESPECIAL = (
    ("AVP", "AVP"),("AVC", "AVC"),("CLP", "CLP"),("CDL", "CDL")
)

class ControlesEspeciais(models.Model):
    prescricaodeenfermagem = models.ForeignKey(PrescricaoDeEnfermagem, on_delete=models.CASCADE)
    tipo = models.CharField(max_length = 4, choices = TIPOS_CONTROLE_ESPECIAL)
    data = models.DateField(auto_now_add=True)
    acao = models.CharField(max_length = 1, choices = ( ("Colocado", "c"), ("Trocado", "t") ))



class TipoSinalVital(models.Model):
    nome = models.CharField(max_length = 255)

class SinaisVitais(models.Model):
    Prontuario = models.ForeignKey(PrescricaoDeEnfermagem, on_delete=models.CASCADE)
    tiposinalvital = models.ForeignKey(TipoSinalVital, on_delete = models.CASCADE)
    valor = models.CharField(max_length = 255)
    marcado = models.BooleanField(default = False)



class Especialidade(models.Model):
    nome = models.CharField(max_length = 1)
