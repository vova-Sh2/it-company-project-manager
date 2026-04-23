from django.urls import path

from task_manager.views import index, TaskListView, WorkerListView, account_info

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("works/", WorkerListView.as_view(), name="worker-list"),
    path("account_info/", account_info, name="account-info"),

]

app_name = "task_manager"
