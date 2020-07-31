from django.shortcuts import render, redirect
from django.urls import reverse

from .models import *

def beforehome(request):
    return render(request, 'piroquiz/beforehome.html')

# Create your views here.
def CreateQuiz(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        schoolans = request.POST.get('school')
        foodans = request.POST.get('food')
        answer = Answer.objects.create(
            title=title,
            schoolans=schoolans,
            foodans=foodans
        )

        url = reverse('piroquiz:index')
        return redirect(to=url)

    return render(request,'piroquiz/createQuiz.html')

def index(request):
    qs = Answer.objects.all()

    return render(request,'piroquiz/index.html', {'lists': qs})

def DetailQuiz(request):
    return render(request,'piroquiz/detailQuiz.html')


def SolveQuiz(request, pk):
    if request.method == 'POST':
        schoolans = request.POST.get('school')
        foodans = request.POST.get('food')
        correct = Correct.objects.create(
            schoolans=schoolans,
            foodans=foodans
        )

        url = reverse('piroquiz:index')
        return redirect(to=url)
    answer = Answer.objects.get(pk=pk)
    return render(request,'piroquiz/SolveQuiz.html', {'answer': answer})

