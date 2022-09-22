from urllib.parse import urlparse
from rest_framework import routers
from .api import PacienteViewSet

router = routers.DefaultRouter()

router.register('api/projects', PacienteViewSet, 'project')

urlpatterns = router.urls