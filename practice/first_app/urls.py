from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='app'),
    path('service/',views.service,name='service'),
    path('form/',views.form,name='form'),
    path('about/',views.about,name='about'),
    path('/django',views.django,name='django'),]