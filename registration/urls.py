from django.urls import path,include
from . import views
from rest_framework import routers
from .views import *
from django.contrib import admin

# router= routers.DefaultRouter()
# router.register(r'sikapay',TableViewSet)


urlpatterns=[
   
    path('api-auth/', include('rest_framework.urls')),
    path('', views.login, name='login'),
    path('signup.html', views.signup, name='signup'),
    path('dashboard.html', views.dashboard, name='dashboard'),
    path('about-us.html', views.aboutus, name='about-us'),
    
    path('businessregform.html', views.businessregform, name='businessregform'),

    
]