from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic, View
from django.views.decorators.csrf import csrf_exempt

from todo.forms import TaskForm
from todo.models import Tag, Task


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    success_url = reverse_lazy("todo:task-list")
    form_class = TaskForm


class TaskUpdateView(generic.UpdateView):
    model = Task
    success_url = reverse_lazy("todo:task-list")
    form_class = TaskForm


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")


@method_decorator(csrf_exempt, name='post')
class ToggleTaskStatusView(View):
    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=self.kwargs['pk'])
        task.status = not task.status
        task.save()
        return redirect(reverse_lazy("todo:task-list"))
