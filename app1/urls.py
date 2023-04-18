from django.urls import path
from . import views
urlpatterns = [
   
    path('',views.signup,name='signup'),
    path('login',views.LoginPage,name='login'),
    # path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('app/',views.app,name='app'),
]