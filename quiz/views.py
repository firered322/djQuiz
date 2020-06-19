from django.shortcuts import render
from .models import Question


def home(request):
    question = Question.objects.get(id=1)
    context = {'question': question}
    return render(request, 'quiz/home.html', context)
