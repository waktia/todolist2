
from django.contrib import admin
from django.urls import path
from .views import Todolist, TodoCreate, TodoDetail

urlpatterns = [

    path("list/", Todolist.as_view(), name="list"),
    path("create/", TodoCreate.as_view(), name="create"),
    path("detail/<int:pk>", TodoDetail.as_view(), name="detail"),
]
