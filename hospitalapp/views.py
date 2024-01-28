from django.shortcuts import render
from django.http import HttpResponse
from .models import  Deparments
from .models import Doctors
from .forms import Bookingform
# Create your views here.


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,"about.html")

def Booking(request):
    if request.method == "POST":
        form = Bookingform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"confirmation.html")
    form = Bookingform()
    dict_form={
        'form': form
    }
    return render(request,"booking.html",dict_form)

def Doctorspage(request):
    dict_doc = {
        "doc":Doctors.objects.all()
    }
    return render(request,"doctors.html",dict_doc)

def Contact(request):
    return render(request,"contact.html")

def Department(request):
    dict_dept={
        "dept":Deparments.objects.all()
    }
    return render(request,"department.html",dict_dept)


