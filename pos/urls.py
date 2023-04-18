"""ems URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from os import set_inheritable
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from backend.views import CreateCheckoutSessionView, ProductLandingPage, CancelView, SuccessView, stripe_webhook, StripeIntentView

from core.views import HomeView


urlpatterns = [
    path('admin/', admin.site.urls,name="admin-site"),
    path('hghhghh/', include('app1.urls')),
    path('', include('dashboard.urls')),
    path('posApp/', include('posApp.urls')),
    path('store/', include('store.urls')),
  
   
   
    path('accounts/', include('accounts.urls')),
   
    path(
        'transaction/',
        include('transactions.urls', namespace='transactions')),
   

    path('mirai/', include('mirai.urls', namespace='mirai')),

    path('backend/', include('backend.urls')),
    path('create-chectout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('create-payment-intent/<pk>/', StripeIntentView.as_view(), name='create-payment-intent'),
    path('success/', SuccessView.as_view(), name='success'),
    path('webhooks/stripe/', stripe_webhook, name='stripe-webhook'),  #doesn't use .as_view()
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('hjj', ProductLandingPage.as_view(), name='landing-page')
]
    
    

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
