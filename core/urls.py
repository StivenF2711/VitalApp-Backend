from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import CoreViewSet

router = DefaultRouter()
router.register(r"results", CoreViewSet, basename="results")

urlpatterns = router.urls
