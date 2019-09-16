"""fisio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import  routers
from api import viewsets
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('patient', viewsets.PatientViewSet, base_name='patient_endpoint')
router.register('image-patient', viewsets.ImagePatientViewSet, base_name='image_patient_endpoint')
router.register('appointment', viewsets.AppointmentViewSet, base_name='appointment_endpoint')
router.register('appointments', viewsets.AppointmentsViewSet, base_name='appointments_endpoint')
router.register('diagnostic', viewsets.DiagnosticViewSet, base_name='diagnostic_endpoint')
router.register('image-diagnostic', viewsets.ImageDiagnosticViewSet, base_name='image_diagnostic_endpoint')
router.register('agreement', viewsets.AgreementViewSet, base_name='agreement_endpoint')
router.register('billstopay', viewsets.BillsToPayViewSet, base_name='billstopay_endpoint')
router.register('billstoreceive', viewsets.BillsToReceiveViewSet, base_name='billstoreceive')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v0/', include(router.urls)),
    path('api-auth/', obtain_auth_token)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
