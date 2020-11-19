from django.shortcuts import render, redirect
from .models import solution, SignUpForm
from django.views import generic
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.db.models import Q

from django.core.paginator import Paginator

class SolutionList(generic.ListView):
    queryset = solution.objects.all()
    paginate_by = 5
    template_name = 'index.html'


class SolutionDetail(generic.DetailView):

    model = solution
    template_name = 'solution_detail.html'



def register(request):
   return render(request,'Signup.html')


def searchResultView(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(title__icontains=query) | Q(problemStatement__icontains=query) | Q(group__icontains=query)

            results= solution.objects.filter(lookups).distinct()

            context={'results': results, 'submitbutton': submitbutton}

            return render(request, 'searchResults.html', context)

        else:
            return render(request, 'index.html')

    else:
        return render(request, 'index.html')



############### Domain Selection Routings #################

class Datastructures(generic.ListView):
    queryset = solution.objects.filter(group = 'datastructures')
    paginate_by = 5
    template_name = 'index.html'

class Algorithms(generic.ListView):
    queryset = solution.objects.filter(group = 'algorithms')
    paginate_by = 5
    template_name = 'index.html'

class ProblemSolving(generic.ListView):
    queryset = solution.objects.filter(group = 'problemsolving')
    paginate_by = 5
    template_name = 'index.html'

class Python(generic.ListView):
    queryset = solution.objects.filter(group = 'python')
    paginate_by = 5
    template_name = 'index.html'

class Java(generic.ListView):
    queryset = solution.objects.filter(group = 'java')
    paginate_by = 5
    template_name = 'index.html'


class Interview(generic.ListView):
    queryset = solution.objects.filter(group = 'interview')
    paginate_by = 5
    template_name = 'index.html'

class C(generic.ListView):
    queryset = solution.objects.filter(group = 'c')
    paginate_by = 5
    template_name = 'index.html'


class CCC(generic.ListView):
    queryset = solution.objects.filter(group = 'c++')
    paginate_by = 5
    template_name = 'index.html'
