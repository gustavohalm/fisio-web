from django.urls import path
from . import views

urlpatterns = [
    path('consultas', views.ListView.as_view(), name='list_appointment')
]