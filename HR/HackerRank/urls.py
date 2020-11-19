from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('accounts/', include('allauth.urls')),
    url(r'^sitemap.xml/$', TemplateView.as_view(template_name='sitemap.xml'), name='sitemaps'),
    url(r'^python.xml/$', TemplateView.as_view(template_name='python.xml'), name='pythonsitemaps'),
    url(r'^java.xml/$', TemplateView.as_view(template_name='java.xml'), name='javasitemaps'),
    url(r'^c.xml/$', TemplateView.as_view(template_name='c.xml'), name='csitemaps'),
    url(r'^ccc.xml/$', TemplateView.as_view(template_name='ccc.xml'), name='cccsitemaps'),
    url(r'^ds.xml/$', TemplateView.as_view(template_name='ds.xml'), name='dssitemaps'),
    url(r'^algo.xml/$', TemplateView.as_view(template_name='algo.xml'), name='algositemaps'),
    url(r'^interview.xml/$', TemplateView.as_view(template_name='interview.xml'), name='interviewsitemaps'),



    
]
