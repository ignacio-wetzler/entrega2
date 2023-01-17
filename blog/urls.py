"""django_blogg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
from django.urls import path
from .views import VistaDeLista, PostDetailView, CrearPost, ModificarPost, PostDeleteView, comentario
from . import views


urlpatterns = [
    path("", views.home , name= "blog-home"),
    path("about", views.about, name= "blog-about"),
    path("post/<int:pk>/", PostDetailView.as_view(), name= "post-detail"),
    path("post/<int:pk>/update/", ModificarPost.as_view(), name = "post-modificar"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name = "post-delete"),
    path("post/<int:pk>/coment/", views.comentario, name = "post-coment"),
    path("post/new/", CrearPost.as_view(), name = "post-form"),
]