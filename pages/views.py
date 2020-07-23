from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
import captcha
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
            send_mail(subject=f'ensardemirci.com İletişim - {sender_email} ', message=message, from_email=sender_email, recipient_list=['ensardemirci93@gmail.com'])
            messages.add_message(request, messages.SUCCESS, ('Mesaj Gönderildi.'))
            return render(request, 'pages/contact.html', {'form': form})
    else:
        form = ContactForm()
    return render(request, 'pages/contact.html', {'form': form})


