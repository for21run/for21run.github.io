from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact),
#	path('articles/', include('articles.urls')),
	path('articles/', views.articles, name='articles'),
    path('admin/', admin.site.urls),
]
