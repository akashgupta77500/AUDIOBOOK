
from django.shortcuts import render,redirect
import pyttsx3
from espeakng import ESpeakNG

# Create your views here.


def index(request):
    return render(request,'index.html')


def resumeread(request):
    if request.method == "POST" :
        value = request.POST["honey"]
        engine = pyttsx3.init()
        engine.say(value)
        engine.runAndWait()
        return redirect('/')



