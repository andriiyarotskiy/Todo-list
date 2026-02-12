from django.urls import path

from todo.views import (
    TaskListView,
    TaskCreateView,
    TaskDeleteView,
    TaskUpdateView,
    TagDeleteView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    toggle_task_complete,
)

urlpatterns = [
    # Tasks
    path("", TaskListView.as_view(), name="task-list"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/toggle-complete/", toggle_task_complete, name="toggle-complete"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    # Tags
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "todo"
