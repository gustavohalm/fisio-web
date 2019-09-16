from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Patient)
admin.site.register(models.Agreement)
admin.site.register(models.Appointment)
admin.site.register(models.Diagnostic)
admin.site.register(models.Procedure)
admin.site.register(models.FieldDiagnostic)
admin.site.register(models.BillToRecieve)
admin.site.register(models.BillToPay)
admin.site.register(models.ImageDiagnostic)
admin.site.register(models.ImageProfile)