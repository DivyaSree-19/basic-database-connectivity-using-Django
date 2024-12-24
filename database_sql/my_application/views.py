from django.shortcuts import render
from django.http import HttpResponse
from .models import data

# Create your views here.
def home(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']     
        mail=request.POST['mail']

        obj=data()
        obj.Name=name
        obj.Age=age
        obj.Address=address
        obj.Mail=mail
        obj.save()



    return render(request,'home.html')
