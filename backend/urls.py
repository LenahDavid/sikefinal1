from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import RegisterUserViewSet

from . import views

router = DefaultRouter()
router.register('signup', RegisterUserViewSet, basename='signup')

urlpatterns = [
    path('api/', include(router.urls)),
   
]