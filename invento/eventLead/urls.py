from django.urls import path
from ticketList import views
from eventLead import views

urlpatterns = [   
    path('eventLeadView',views.eventLeadView, name='eventLeadView'),
    path('unredeem', views.unredeem, name='unredeem'),
]
 