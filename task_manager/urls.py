from django.urls import path

from task_manager.views import (
    index,
    TaskListView,
    WorkerListView,
    account_info,
    TaskDetailView,
    task_complete,
    TaskCreateView,
    WorkerCreateView,
    TaskTypeCreateView,
    PositionCreateView, TaskDeleteView, TaskTypeListView, TaskTypeUpdateView, TaskTypeDeleteView,
    WorkerPositionUpdateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>", TaskDetailView.as_view(), name="task-detail"),

    path("tasks/<int:pk>/complete", task_complete, name="task_complete"),
    path("task_types/", TaskTypeListView.as_view(), name="task-type"),
    path("task_types/<int:pk>/update/", TaskTypeUpdateView.as_view(), name="task-type-update"),
    path("task_types/<int:pk>/deleta/", TaskTypeDeleteView.as_view(), name="task-type-delete"),
    path("task_types/create/", TaskTypeCreateView.as_view(), name="task-type-create"),

    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/create", WorkerCreateView.as_view(), name="worker-create"),
    path("workers/<int:pk>/position_update", WorkerPositionUpdateView.as_view(), name="worker-position-update"),
    path("workers/<int:pk>/delete", WorkerCreateView.as_view(), name="worker-delete"),
    path("position/create", PositionCreateView.as_view(), name="position-create"),
    path("account_info/", account_info, name="account-info"),

]

app_name = "task_manager"
