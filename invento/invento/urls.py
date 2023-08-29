"""
URL configuration for invento project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from ticketList import views

urlpatterns = [
    path('admin/', admin.site.urls),    
    
    path('', views.index, name='home'),
    path('new', views.addTkt, name='addticket'),
    path('upload', views.upload, name='upload'),
    path('redeem', views.redeem, name='redeem'),
    path('signin', views.signin, name='signin'),
    path('invento_login', views.invento_login, name='invento_login'),
    path('invento_logout', views.invento_logout, name='invento_logout'),
    path('search_ticket', views.search_ticket, name='search_ticket'),
    path('delete', views.delete, name='delete'),
]
 