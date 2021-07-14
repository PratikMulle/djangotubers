from django.shortcuts import render, redirect
from .models import ContactTeam
from django.contrib import messages

# Create your views here.
def contactteam(request):
    if request.method == "POST":
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        email = request.POST['email']
        company_name = request.POST['company_name']
        subject = request.POST['subject']
        message = request.POST['message']

    contactteam = ContactTeam(full_name=full_name, phone=phone, email=email, company_name=company_name, subject=subject, message=message)
    contactteam.save()
    messages.success(request, 'Thanks for reching out !')
    
    return redirect('webpages')