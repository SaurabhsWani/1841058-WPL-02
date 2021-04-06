from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
# def homePageView(request):
	# return HttpResponse('Hello, This is Saurabh Sunil Wani From T4 Batch and my PRN is 1841058')
class HomePageView(TemplateView):
	template_name='home.html'
class AboutPageView(TemplateView):#new
	template_name='about.html'
class ContactPageView(TemplateView):#new
	template_name='contact.html'