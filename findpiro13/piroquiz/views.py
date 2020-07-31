from django.shortcuts import render

def beforehome(request):
    return render(request, 'piroquiz/beforehome.html')

def home(request):
    return render(request,'piroquiz/home.html')

def CreateQuiz(request):
    return render(request,'piroquiz/createQuiz.html')

def index(request):
    return render(request,'piroquiz/index.html')

def DetailQuiz(request):
    return render(request,'piroquiz/detailQuiz.html')

def SolveQuiz(request):
    return render(request, 'piroquiz/solveQuiz.html')

