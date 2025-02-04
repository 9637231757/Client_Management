# clients/urls.py
"""from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ProjectViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'projects', ProjectViewSet, basename='project')

urlpatterns = [
    path('api/', include(router.urls)),
]"""

from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ProjectViewSet

# Set up the router to register viewsets
router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'projects', ProjectViewSet, basename='project')

# Return router URLs directly
urlpatterns = router.urls

