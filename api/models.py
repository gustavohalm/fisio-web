from django.db import models
from django.contrib.auth.models import  User
# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=556)
    height = models.DecimalField(max_digits=3, decimal_places=2)
    weight = models.DecimalField(max_digits=4, decimal_places=2)
    email = models.CharField(max_length=500)
    celphone = models.CharField(max_length=13)
    addres_1 = models.CharField(max_length=322)
    addres_2 = models.CharField(max_length=322)
    addres_3 = models.CharField(max_length=322)
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=48)
    agreement = models.ForeignKey('Agreement', blank=True, null=True, on_delete=models.PROTECT)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=11)
    born = models.DateField()
    description = models.TextField()
    fisio = models.ForeignKey('auth.User', on_delete=models.CASCADE)

class Appointment(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.PROTECT)
    day = models.DateField()
    time = models.TimeField()
    value = models.DecimalField(max_digits=8,decimal_places=2)
    fisio = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('Pendente', 'Pendente'),
        ('Faltou', 'Faltou'),
        ('Realizado','Realizado')
     
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=32, null=True,blank=True)


class Procedure(models.Model):
    name = models.CharField(max_length=256)
    value = models.DecimalField(max_digits=8, decimal_places=2)
    fisio = models.ForeignKey('auth.User', on_delete=models.CASCADE)


class Diagnostic(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    appointment = models.ForeignKey('Appointment', blank=True, null=True, on_delete=models.CASCADE)
    fisio = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    anamnese = models.CharField(max_length=1024, blank=True, null=True)
    fowarding = models.CharField(max_length=1024, blank=True, null=True)
    qp = models.CharField(max_length=1024, blank=True, null=True)
    hma = models.CharField(max_length=1024, blank=True, null=True)
    hmf = models.CharField(max_length=1024, blank=True, null=True)
    hmp = models.CharField(max_length=1024, blank=True, null=True)
    medication = models.CharField(max_length=1024, blank=True, null=True)
    evolution = models.CharField(max_length=512,blank=True, null=True)
    observation = models.CharField(max_length=1024, blank=True, null=True)    
    functional = models.CharField(max_length=1024, blank=True, null=True)
    trainning = models.CharField(max_length=1024, blank=True, null=True)
    physic_exam = models.CharField(max_length=512, blank=True, null=True)

    def get_diagnostics(self):  
        return self.diagnostics.all()

class FieldDiagnostic(models.Model):
    diagnostic = models.ForeignKey('Diagnostic', on_delete=models.CASCADE, related_name='diagnostics')
    procedure = models.ForeignKey('Procedure', on_delete=models.CASCADE)
    text = models.CharField(max_length=1024)

class Agreement(models.Model):
    name = models.CharField(max_length=256)
    value = models.DecimalField(max_digits=8,decimal_places=2,blank=True, null=True)
    percent = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    fisio = models.ForeignKey('auth.User', on_delete=models.CASCADE)

class ImageDiagnostic(models.Model):
    diagnostic = models.ForeignKey('Diagnostic', on_delete=models.CASCADE)
    url = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=512, blank=True, null=True)
    fisio = models.ForeignKey('auth.User', on_delete=models.CASCADE)

class ImageProfile(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    url = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=512, blank=True, null=True)
    fisio = models.ForeignKey('auth.User', on_delete=models.CASCADE)



class BillToPay(models.Model):
    value = models.DecimalField(max_digits=8,decimal_places=2)
    date  = models.DateField()
    description = models.CharField(max_length=256)
    fisio = models.ForeignKey('auth.User', on_delete=models.CASCADE)

class BillToRecieve(models.Model):
    value = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    fisio = models.ForeignKey('auth.User', on_delete=models.CASCADE)

