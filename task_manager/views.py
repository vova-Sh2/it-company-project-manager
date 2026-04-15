from django.shortcuts import render
from django.views import generic

from task_manager.models import Task, Worker


def index(request):
    """View function for the home page of the site."""
    num_uncompleted_tasks = Task.objects.all().filter(is_completed=False).count()
    num_completed_tasks = Task.objects.all().filter(is_completed=True).count()
    context = {
        "num_uncompleted_tasks": num_uncompleted_tasks,
        "num_completed_tasks": num_completed_tasks,
    }

    return render(request, "task_manager/index.html", context=context)


class TaskListView(generic.ListView):
    model = Task

    def get_queryset(self):
        return Task.objects.filter(assignees=self.request.user)


class WorkerListView(generic.ListView):
    model = Worker
    context_object_name = "worker_list"

