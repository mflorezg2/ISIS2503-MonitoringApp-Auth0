from django.urls import path, include
from rest_framework import routers
from .views import PacienteViewSet, patient_list, patient_create, patient_detail

router = routers.DefaultRouter()
router.register(r'pacientes', PacienteViewSet, basename='paciente')

urlpatterns = [
    # API REST
    path('api/', include(router.urls)),

    # HTML
    path('patients/', patient_list,   name='patient_list'),
    path('patients/create/', patient_create, name='patient_create'),
    path('patients/<int:pk>/', patient_detail, name='patient_detail'),
]
