
from django.shortcuts import render, redirect
from .models import Course as c

def index(request):
    if 'name' not in request.session:
        request.session['name']=''
        request.session['description']=''
    courses = c.objects.all()

    context = { 'courses': courses}
    return render (request,'addcourse/index.html', context)

def show(request):
    request.session['name']=request.POST['name']
    request.session['description']=request.POST['description']

    # print request.POST
    c.objects.create(course_name=request.session['name'], description=request.session['description'])
    courselist = c.objects.all()
    print courselist
    print courselist

    context={'courselist':courselist}
    return redirect ('/')
    # return render (request,'addcourse/success.html', context)

# Create your views here.
