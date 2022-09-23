#from urllib.parse import urlparse
from rest_framework import routers
#from django.conf.urls import url, include
from .api import PacienteViewSet, PhoneViewSet, PacientePhoneViewSet
#from .views import PacienteViewSet, PhoneViewSet
from rest_framework.routers import DefaultRouter

router = routers.DefaultRouter()

router.register('api/pacientes', PacienteViewSet, 'Paciente')
router.register('api/phones', PhoneViewSet, 'Phones')
router.register('api/pacientephone', PacientePhoneViewSet, 'Phones')

urlpatterns = router.urls