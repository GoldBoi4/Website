from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('about', views.about, name='about me'),
    path('services', views.services, name='Services'),
    path('service1', views.service1, name='Server-1'),
    path('service2', views.service2, name='Service-2'),
    path('service3', views.service3, name='Service-3'),
    path('contact', views.contact, name='Contact US'),
    path('files', views.files, name='Files'),
    path('main', views.main, name='CodeOrg'),
    path('blog', views.blog, name='Blog'),
    path('blog1', views.blog1, name='Blog-1'),
    path('blog2', views.blog2, name='Blog-2'),
    path('blog3', views.blog3, name='Blog-3'),
    path('products', views.products, name='Products'),

]
