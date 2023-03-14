from django.shortcuts import render, HttpResponse
from .models import Student
# Create your views here.

# def welcome(request):    # business logic is written here in views.py --request is reserved keyword--http request
    # print(request.GET['name'])   http://127.0.0.1:8000/welcome/?name=abc&age=30
    # print(request.method)
    # print(request.user)
    # print(request.__dict__)
    # stud = Student.objects.values_list('name')
    # l1 = [i for i in stud]
    # return HttpResponse(f"Welcome to django application..!!!")

def welcome(request):
    return render(request, "home.html")