from django.shortcuts import render
from .models import Question


def home(request):
    question = Question.objects.get(id=1)
    answers = question.answer_set.all()
    context = {'question': question, 'answers': answers}
    # print(answers)
    return render(request, 'quiz/home.html', context)
