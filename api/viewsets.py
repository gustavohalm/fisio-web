from . import  serializers, models
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PatientSerializer
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        return models.Patient.objects.filter(fisio=self.request.user)

    def perform_create(self, serializer):
        serializer.save(fisio=self.request.user)

class AppointmentViewSet(viewsets.ModelViewSet):
    serializer_class =  serializers.AppointmentSerializer
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        if 'day' in self.request.GET:
            day = self.request.GET['day']
            return models.Appointment.objects.filter(day=day, fisio=self.request.user).order_by('-time')
        return models.Appointment.objects.all()

    def perform_create(self, serializer):
        serializer.save(fisio=self.request.user)

class AppointmentsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AppointmentsSerializer

    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        if 'day' in self.request.GET:
            day = self.request.GET['day']
            return models.Appointment.objects.filter(day=day, fisio=self.request.user).order_by('-time')
        return models.Appointment.objects.all()

class DiagnosticViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DiagnosticSerializer
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        if 'patient' in self.request.GET:
            patient = self.request.GET['patient']
            return models.Diagnostic.objects.filter(patient=patient)
        return models.Diagnostic.objects.filter(fisio=self.request.user)

    def perform_create(self, serializer):
        serializer.save(fisio=self.request.user)

class FieldDiagnosticsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FieldDiagnosticsSerializer
    permission_classes = (IsAuthenticated, )
    def get_queryset(self):
        if 'diagnostic' in self.request.GET:
            diagnostic = self.request.GET['diagnostic']
            return models.FieldDiagnostic.objects.filter(diagnostic=diagnostic)

class FieldDiagnosticViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FieldDiagnosticSerializer
    permission_classes = (IsAuthenticated, )
    
    

class AgreementViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AgreeementSerializer
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        return models.Agreement.objects.filter(fisio=self.request.user)

    def perform_create(self, serializer):
        serializer.save(fisio=self.request.user)


class BillsToPayViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BillToPaySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        date = self.request.GET['date']
        month = date.split('-')[0]
        year = date.split('-')[1]
        return models.BillToPay.objects.filter(fisio=self.request.user, date__year=year).filter(date__month=month)

    def perform_create(self, serializer):
        serializer.save(fisio=self.request.user)


class BillsToReceiveViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BillToReceiveSerializer
    permission_classes = (IsAuthenticated,)


    def get_queryset(self):
        date = self.request.GET['date']
        month = date.split('-')[0]
        year = date.split('-')[1]

        return models.BillToRecieve.objects.filter(fisio=self.request.user, date__year=year).filter(date__month=month)

    def perform_create(self, serializer):
        serializer.save(fisio=self.request.user)


class ImageDiagnosticViewSet(viewsets.ModelViewSet):
    serializer_class =  serializers.ImageDiagnosticSerialiazer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        diagnostic = self.request.GET['diagnostic']
        return models.ImageDiagnostic.objects.filter(diagnostic=diagnostic)

    def perform_create(self, serializer):
        serializer.save(fisio=self.request.user)


class ImagePatientViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ImagePatientSerialiazer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        patient = self.request.GET['patient']
        return models.ImageProfile.objects.filter(patient=patient)

    def perform_create(self, serializer):
        serializer.save(fisio=self.request.user)
