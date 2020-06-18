from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    question = models.CharField(max_length=200)
    correct_ans = models.CharField(max_length=200)
    wrong_ans1 = models.CharField(max_length=200)
    wrong_ans2 = models.CharField(max_length=200)

    def __str__(self):
        return self.question
