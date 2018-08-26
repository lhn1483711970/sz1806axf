"""sz1806axf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('market/', views.market),

   path('shopcar/', views.shopcar),
    path('mine/', views.mine),
    path('regist_jyname/', views.regist_jyname),
    path('regist/', views.regist),
    path('login/', views.login),
    path('yzcode/', views.yzcode),
    path('addshopcar/', views.addshopcar),


]
