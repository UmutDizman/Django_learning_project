from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseNotFound

# Create your views here.
course_dictionarry = {
    "python": "Python Course Page",
    "java": "Java course page",
    "css" :   "CSS course Page"
}

def index(request):
    return HttpResponse("First django project")

def course(request, item):
    try:
        course = course_dictionarry[item]
        return HttpResponse(course)
    except:
        return HttpResponseNotFound("page not found please try another course")
        #raise Http404("page not found please try another course")
        #return HttpResponse(course_dictionarry[item])

def multiply_wievs(request, num1,num2):
    return HttpResponse(f"{num1} * {num2} = {num1 *num2}")