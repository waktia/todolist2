from todo.models import TodoModel
from django.shortcuts import render
from .models import TodoModel
from django.views.generic import ListView


# Create your views here.

class Todolist(ListView):
  template_name = "list.html"
  model = TodoModel
