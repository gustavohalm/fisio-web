from rest_framework import serializers
from . import  models


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient
        fields = ['id', 'name', 'email','height', 'weight', 'celphone', 'addres_1', 'addres_2', 'addres_3', 'city', 'state', 'agreement', 'cpf','rg' ,'born', 'description', 'fisio']
        read_only_fields = ('id',  'fisio')


class AgreeementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Agreement
        fields = ['id', 'name', 'value', 'percent', 'fisio']
        read_only_fields = ('id',  'fisio')


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Appointment
        fields = ['id', 'patient', 'day', 'time','status', 'value', 'fisio']
        read_only_fields = ('id',  'fisio')


class AppointmentsSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=False, many=False)

    class Meta:
        model = models.Appointment
        fields = ['id', 'patient', 'day', 'time','status', 'value', 'fisio']
        read_only_fields = ('id',  'fisio')
    

class ProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Procedure
        fields = ['id', 'name', 'value', 'fisio']
        read_only_fields = ['id',  'fisio']


class DiagnosticSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Diagnostic
        fields = '__all__'
        read_only_fields = ('id',  'fisio')


class DiagnosticNestedSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(many=False)
    appointment = AppointmentSerializer(many=False)
    class Meta:
        model = models.Diagnostic
        fields = '__all__'


class FieldDiagnosticsSerializer(serializers.ModelSerializer):
    procedure = ProcedureSerializer(read_only=False, many=False)

    class Meta:
        model = models.FieldDiagnostic
        fields = ['id', 'procedure', 'diagnostic', 'text']
        read_only_fields = ('id', )


class FieldDiagnosticSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FieldDiagnostic
        fields = ['id', 'procedure', 'diagnostic', 'text']
        read_only_fields = ('id', )


class BillToPaySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BillToPay
        fields = ['id', 'value', 'description','date', 'fisio']
        read_only_fields = ('id',  'fisio')


class BillToReceiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BillToRecieve
        fields = ['id', 'value', 'date', 'fisio', 'patient']
        read_only_fields = ('id',  'fisio')


class ImagePatientSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = models.ImageProfile
        fields = ['id', 'patient', 'url', 'description', 'fisio']
        read_only_fields = ('id',  'fisio')


class ImageDiagnosticSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = models.ImageProfile
        fields = ['id', 'diagnostic', 'url', 'description', 'fisio']
        read_only_fields = ('id',  'fisio')
