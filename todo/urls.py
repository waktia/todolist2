
from django.contrib import admin
from django.urls import path
from .views import Todolist, TodoCreate

urlpatterns = [

    path("list/", Todolist.as_view(), name="list"),
    path("create/", TodoCreate.as_view(), name="create"),

]
