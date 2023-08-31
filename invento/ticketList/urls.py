from django.urls import path
from ticketList import views

urlpatterns = [   
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
 