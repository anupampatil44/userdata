from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .forms import Register
from .models import Data

def register(request):

    if request.method == 'POST':  # data sent by user
        first=request.POST['fname']
        last =request.POST['lname']
        email=request.POST['email']
        gender=request.POST['gender']
        form = Data(first=first,last=last,email=email,gender=gender)
        form.save()

    return render(request,"users/signup.html",)

def search(request):
    if request.method == 'POST':
        email=request.POST['email']
        global form
        try:
            profile=Data.objects.get(email=email)
            return render(request,"users/found.html",{'profile':profile})
        except:
            return render(request, "users/error.html")
    else:
        return render(request,"users/search.html",)


