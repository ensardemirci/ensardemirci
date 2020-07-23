from django import forms
from captcha.fields import CaptchaField

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label= 'İsim')
    email = forms.EmailField(label='E-Mail')
    message = forms.CharField(widget=forms.Textarea, label='Mesaj')
    captcha = CaptchaField()
