

from todo.models import TodoModel
from django.shortcuts import render
from .models import TodoModel
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.

class Todolist(ListView):
  template_name = "list.html"
  model = TodoModel

class TodoCreate(CreateView):
  template_name= "create.html"
  model = TodoModel
  fields = ("title", "content", "duedate")
  success_url = reverse_lazy("list")

class TodoDetail(DetailView):
  template_name = "detail.html"
  model= TodoModel

class TodoUpdate(UpdateView):
  template_name = "update.html"
  model = TodoModel
  fields = ("title", "content", "duedate")
  success_url = reverse_lazy("list")

class TodoDelete(DeleteView):
  template_name = "delete.html"
  model= TodoModel
  success_url = reverse_lazy("list")
