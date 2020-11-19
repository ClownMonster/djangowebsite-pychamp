from django.urls import path
from .views import SolutionDetail,SolutionList,Datastructures,Algorithms,Python
from .views import Java,C,CCC,Interview,ProblemSolving,searchResultView
from django.conf.urls import url



from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',SolutionList.as_view(),name='solutionList'),
    path('<slug:slug>/',SolutionDetail.as_view(),name='solutionDetail'),
    path('search/results',searchResultView, name = 'search'),
    url(r'^accounts/logout/$', auth_views.LogoutView.as_view(template_name = 'Loggedout.html'),name='logout'),
    #url(r'^accounts/social/signup/$',views.register,name='signup'),
    url(r'language/python',Python.as_view(), name='Python'),
    url(r'language/java',Java.as_view(), name='Java'),
    url(r'language/c',C.as_view(), name='C'),
    url(r'language/CCC',CCC.as_view(), name='C++'),
    url(r'language/problemsolving',ProblemSolving.as_view(), name='ProblemSolving'),
    url(r'language/interviewprep',Interview.as_view(), name='Interview'),
    url(r'language/Datastructures',Datastructures.as_view(), name='Datastructures'),
    url(r'language/Algrithms',Algorithms.as_view(), name='Algorithms'),



] 