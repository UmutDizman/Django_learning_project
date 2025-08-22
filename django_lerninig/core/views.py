from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
course_dictionarry = {
    "python": "Python Course Page",
    "java": "Java course page",
    "css" :   "CSS course Page"
}

def index(request):
    return HttpResponse("First django project")

def course(request, item):
    return HttpResponse(course_dictionarry[item])

def multiply_wievs(request, num1,num2):
    return HttpResponse(f"{num1} * {num2} = {num1 *num2}")