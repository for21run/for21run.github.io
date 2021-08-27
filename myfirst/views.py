from django.http import HttpResponse
from django.shortcuts import render


def home(request):
#	return HttpResponse("<h1>main page</h1>")
	return render(request, 'myfirst/mainpage.html')


def about(request):
	return render(request, 'myfirst/about.html')


def contact(request):
	return render(request, 'myfirst/contact.html')

	
def articles(request):
	return render(request, 'myfirst/articles.html')
		