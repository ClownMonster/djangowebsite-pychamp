from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms



class solution(models.Model):
    title = models.CharField(max_length=200, blank=False)

    # for domain selection
    choice = (('datastructures','datastructures'),
              ('algorithms','algorithms'),
              ('problemsolving','problemsolving'),
              ('python','python'),
              ('java','java'),
              ('interview','interview'),
              ('c','c'),
              ('c++','c++'))

    group = models.CharField(max_length=30, choices=choice, default='choose')

    # for navigation to detailed view
    slug = models.SlugField(max_length=200, blank=False)

    problemStatement = models.TextField(blank=False)

    solution = models.TextField(blank=False)
    


    def __str__(self):
        return self.title



class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )