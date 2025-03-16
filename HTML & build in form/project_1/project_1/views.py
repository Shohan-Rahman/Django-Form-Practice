from django.shortcuts import render
from . forms import Django_form

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        return render(request,'index.html',{'name' : name, 'email' : email})
    else:
        return render(request,'index.html')
def html_form(request):
    return render(request,'html_form.html')
def build_in_form(request):
    form = Django_form(request.POST)
    return render(request,'build_in_form.html',{'form' : form})