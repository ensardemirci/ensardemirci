from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def blog(request):
    return render(request, 'pages/blog.html')

# def contact(request):
#     return render(request, 'pages/contact.html')

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']

            message = f'İsim : {sender_name} Mesaj : {form.cleaned_data["message"]}'
            send_mail('ed.com Yeni Mesaj', message, sender_email, ['ensardemirci93@gmail.com'])
            return HttpResponse('Teşekkürler Mesajınız Alındı')
    else:
        form = ContactForm()
    return render(request,'pages/contact.html',{'form': form})



