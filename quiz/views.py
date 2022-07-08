from django.shortcuts import render

# Create your views here.

def start_quiz(request):
    return render(request,'quiz/open_me.html')

def index(request):
    return render(request,'quiz/index.html')

def index1(request):
    return render(request,'quiz/index1.html')

def index2(request):
    return render(request,'quiz/index2.html')

def index3(request):
    return render(request,'quiz/index3.html')

def index4(request):
    return render(request,'quiz/index4.html')

def index5(request):
    return render(request,'quiz/index5.html')
