from django.shortcuts import render,redirect
from ticketList.models import ticket_info
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

#functions for passing all data from ticket_info model to index page
@login_required(login_url='invento_login')
def index(request):
    tickets = ticket_info.objects.all()
    return render(request, 'index.html', {'tickets': tickets})


#Functions for activating the add ticket button on the index page
@login_required(login_url='invento_login')
def addTkt(request):
    return render(request, 'newticket.html')    

#Crete new ticket functionality
@login_required(login_url='invento_login')
def upload(request):
    if request.method == 'POST':
        IDtkt = request.POST['number']
        status = request.POST['status']
        if ticket_info.objects.filter(IDtkt=IDtkt).exists():
            return render(request, 'newticket.html', {'error_message': 'Already registered'})
        else :
            ticket = ticket_info.objects.create(IDtkt=IDtkt, status=status)
            ticket.save()
            return render(request, 'newticket.html', {'error_message': 'Registered Successfully submit another ticket'})
    else:
        return redirect('/')

#Redeem ticket functionality implemented here
@login_required(login_url='invento_login')
def redeem(request):
    if request.method == 'POST':
        IDtkt = request.POST['ticket_id']
        status = request.POST['statusupdate']
        ticket = ticket_info.objects.get(IDtkt=IDtkt)
        ticket.status = status
        ticket.save()
        return redirect('/')


#Sign in functionality implemented here using django 
@login_required(login_url='invento_login')
def signin(request):
    return render(request, 'signin.html')

#Code for searching tickets
@login_required(login_url='invento_login')
def search_ticket(request):
    searched_tickets = []
    search_message = ""

    if request.method == 'POST':
        ticket_id = request.POST['ticket_id']
        if ticket_id.isdigit():
            searched_tickets = ticket_info.objects.filter(IDtkt__contains=ticket_id)
            if not searched_tickets:
                search_message = f"No tickets found containing '{ticket_id}'."
        else:
            search_message = "Invalid ticket ID format. Please enter a number."

    tickets = ticket_info.objects.all()
    return render(request, 'index.html', {'tickets': tickets, 'searched_tickets': searched_tickets, 'search_message': search_message})


#code to implement vlunteer login feature
def invento_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else :
            return render(request, 'signin.html', {'error_message': 'Invalid login credentials'})
    else :
        return render(request, 'signin.html')
    

#Code for implementing logout feature
@login_required(login_url='invento_login')
def invento_logout(request):
    logout(request)
    return redirect('invento_login')



#Code for adding delete tickets functionality 
@login_required(login_url='invento_logout')
def delete(request):
    if request.method == 'POST':
        IDtkt = request.POST['ticket_id']
        ticket = ticket_info.objects.get(IDtkt=IDtkt)
        ticket.delete()
        return redirect('/')
