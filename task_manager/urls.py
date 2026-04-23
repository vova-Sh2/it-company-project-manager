from django.urls import path

from task_manager.views import (
    index,
    TaskListView,
    WorkerListView,
    account_info,
    TaskDetailView,
    task_complete,
    TaskCreateView,
    WorkerCreateView, TaskTypeCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>", TaskDetailView.as_view(), name="task-detail"),

    path("tasks/<int:pk>/complete", task_complete, name="task_complete"),
    path("task_types/create/", TaskTypeCreateView.as_view(), name="task-type-create"),

    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/create", WorkerCreateView.as_view(), name="worker-create"),
    path("account_info/", account_info, name="account-info"),

]

app_name = "task_manager"
