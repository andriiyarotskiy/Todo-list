from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.detail import SingleObjectMixin

from todo.forms import TaskForm
from todo.models import Task, Tag


# Tasks
class TaskListView(generic.ListView):
    model = Task
    template_name = "todo/task_list.html"
    queryset = Task.objects.prefetch_related("tags").order_by("completed", "-datetime")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class ToggleTaskComplete(SingleObjectMixin, generic.View):
    model = Task

    def post(self, request, *args, **kwargs):
        task = self.get_object()
        task.completed = not task.completed
        task.save()
        return redirect("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo/confirm_delete.html"
    success_url = reverse_lazy("todo:task-list")


# Tags
class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"


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
    template_name = "todo/confirm_delete.html"
    success_url = reverse_lazy("todo:tag-list")
