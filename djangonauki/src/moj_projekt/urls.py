# moj_projekt/urls.py
"""
URL configuration for moj_projekt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('moja_strona/', include('moja_strona.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import TodoAppView, AddTodo, EditTodo, UpdateTodoItem, DeleteTodo


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TodoAppView, name="todolist"),
    path("todo/", AddTodo, name="addTodo"),
    path('todo/<int:item_id>/delete/', DeleteTodo, name='DeleteTodo'),
    path('todo/<int:item_id>/edit/', EditTodo, name='EditTodo'),
    path('todo/<int:item_id>/update/', UpdateTodoItem, name='UpdateTodo'),

]
