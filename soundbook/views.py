
from django.shortcuts import render,redirect
import pyttsx3
from text_to_speech import speak

# Create your views here.


def index(request):
    return render(request,'index.html')


def resumeread(request):
    if request.method == "POST" :
       value = request.POST["honey"]
       engine = pyttsx3.init('dummy')
       engine.say(value)
       engine.runAndWait()
       return redirect('/')
