from django.shortcuts import render,redirect
from ticketList.models import ticket_info

# Create your views here.

def index(request):
    tickets = ticket_info.objects.all()
    return render(request, 'index.html', {'tickets': tickets})  

def addTkt(request):
    return render(request, 'newticket.html')    

def upload(request):
    if request.method == 'POST':
        IDtkt = request.POST['number']
        name = request.POST['name']
        date = request.POST['date']
        status = request.POST['status']
        ticket = ticket_info.objects.create(
            IDtkt=IDtkt,
            name=name,
            date=date,
            status=status
        )
        ticket.save()
        return redirect('/')
    else:
        return redirect('/')
    
def redeem(request):
    if request.method == 'POST':
        IDtkt = request.POST['ticket_id']
        status = request.POST['statusupdate']
        ticket = ticket_info.objects.get(IDtkt=IDtkt)
        ticket.status = status
        ticket.save()
        return redirect('/')

def delete(request):
    if request.method == 'POST':
        IDtkt = request.POST['ticket_id']
        ticket = ticket_info.objects.get(IDtkt=IDtkt)
        ticket.delete()
        return redirect('/')
