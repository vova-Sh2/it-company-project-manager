from django.urls import path

from task_manager.views import (
    index,
    TaskListView,
    WorkerListView,
    account_info,
    TaskDetailView,
    task_complete,
    TaskCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>", TaskDetailView.as_view(), name="task-detail"),

    path("tasks/<int:pk>/complete", task_complete, name="task_complete"),
    path("works/", WorkerListView.as_view(), name="worker-list"),
    path("account_info/", account_info, name="account-info"),

]

app_name = "task_manager"
