from django.shortcuts import render,redirect
from ticketList.models import ticket_info
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='invento_login')
def eventLeadView(request):
    tickets = ticket_info.objects.all()
    return render(request,'eventLead.html', {'tickets': tickets})

@login_required(login_url='invento_login')
def unredeem(request):
    if request.method == 'POST':
        IDtkt = request.POST['ticket_id']
        status = request.POST['statusupdate']
        ticket = ticket_info.objects.get(IDtkt=IDtkt)
        ticket.status = status
        ticket.save()
        if request.user.is_superuser:
            return redirect('eventLeadView')
        else:
            return redirect('/')
    if request.user.is_superuser:
        return render(request,'eventlead.html', {'tickets': ticket})
    else:
        return render(request,'index.html',  {'tickets': ticket})