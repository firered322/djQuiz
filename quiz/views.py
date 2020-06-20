from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Question
from .forms import CreateUserForm


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('userhome')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Account successfully created")
                return redirect('login')

        context = {'form': form}
        return render(request, 'quiz/register.html', context)


def home(request):
    question = Question.objects.get(id=1)
    answers = question.answer_set.all()
    context = {'question': question, 'answers': answers}
    # print(answers)
    return render(request, 'quiz/home.html', context)


def loginUser(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('userhome')
            else:
                messages.info(request, "Username or password incorrect")
                return render(request, 'quiz/login.html', context)

    return render(request, 'quiz/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def userhome(request):
    # question = Question.objects.get(id=1)
    # answers = question.answer_set.all()
    # context = {'question': question, 'answers': answers}
    # print(answers)
    return render(request, 'quiz/userhome.html')
