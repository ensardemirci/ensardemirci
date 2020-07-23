from django.http import HttpResponse
from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='index'),
    path('ozgecmis', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('iletisim', views.contact_us, name='contact')

]