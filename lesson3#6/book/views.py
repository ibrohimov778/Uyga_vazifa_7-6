from django.shortcuts import render
from .models import Book

def home(request):
    return render(request,'home.html')


def books(request):
    book = Book.objects.all()
    return  render(request,'python.html',{'books':books})

def author(request):
    pass