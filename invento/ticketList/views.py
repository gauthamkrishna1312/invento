from django.shortcuts import render,redirect
from ticketList.models import ticket_info
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='invento_login')
def index(request):
    tickets = ticket_info.objects.all()
    return render(request, 'index.html', {'tickets': tickets})


@login_required(login_url='invento_login')
def addTkt(request):
    return render(request, 'newticket.html')    

@login_required(login_url='invento_login')
def upload(request):
    if request.method == 'POST':
        IDtkt = request.POST['number']
        status = request.POST['status']
        ticket = ticket_info.objects.create(
            IDtkt=IDtkt,
            status=status
        )
        ticket.save()
        return redirect('/')
    else:
        return redirect('/')


@login_required(login_url='invento_login')
def redeem(request):
    if request.method == 'POST':
        IDtkt = request.POST['ticket_id']
        status = request.POST['statusupdate']
        ticket = ticket_info.objects.get(IDtkt=IDtkt)
        ticket.status = status
        ticket.save()
        return redirect('/')


@login_required(login_url='invento_login')
def signin(request):
    return render(request, 'signin.html')


@login_required(login_url='invento_login')
def search_ticket(request):
    searched_tickets = []
    search_message = ""

    if request.method == 'POST':
        ticket_id = request.POST['ticket_id']
        try:
            ticket = ticket_info.objects.get(IDtkt=ticket_id)
            searched_tickets.append(ticket)
        except ticket_info.DoesNotExist:
            search_message = f"Ticket with ID {ticket_id} not found."

    tickets = ticket_info.objects.all()
    return render(request, 'index.html', {'tickets': tickets, 'searched_tickets': searched_tickets, 'search_message': search_message})



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
    

@login_required(login_url='invento_login')
def invento_logout(request):
    logout(request)
    return redirect('invento_login')

#def delete(request):
#    if request.method == 'POST':
#        IDtkt = request.POST['ticket_id']
#        ticket = ticket_info.objects.get(IDtkt=IDtkt)
#        ticket.delete()
#        return redirect('/')
