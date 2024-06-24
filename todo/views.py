from django.shortcuts import render
from django.views import generic

from todo.models import Tag, Task


def index(request):
    return render(request, "base.html")


class TagListView(generic.ListView):
    model = Tag


class TaskListView(generic.ListView):
    model = Task
