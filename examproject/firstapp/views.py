from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def f1 (req):
    return  HttpResponse('<h1>welcome<h1>')
def index(req):
    return render(req,'index.html')
def about(req):
    return render(req,'about.html')
def studentform(req):
    return render(req,'studentform.html')
def contact(req):
    return render(req,'contact.html')
def newhtml(req):
    return render(req,'newhtml.html')
