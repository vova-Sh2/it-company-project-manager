from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from task_manager.forms import TaskForm
from task_manager.models import Task, Worker


@login_required
def index(request):
    """View function for the home page of the site."""
    num_uncompleted_tasks = Task.objects.all().filter(is_completed=False).count()
    num_completed_tasks = Task.objects.all().filter(is_completed=True).count()
    context = {
        "num_uncompleted_tasks": num_uncompleted_tasks,
        "num_completed_tasks": num_completed_tasks,
    }

    return render(request, "task_manager/index.html", context=context)


@login_required
def account_info(request):
    completed_tasks = Task.objects.all().filter(is_completed=True).count()
    context = {
        "completed_tasks": completed_tasks
    }
    return render(request, "account_info/account_info.html" , context=context)

@login_required
def task_complete(request, pk):
    if request.method == "POST":
        obj = Task.objects.get(id=pk)
        obj.is_completed = True
        obj.save()
    return redirect(request.GET.get("next"))




class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 5

    def get_queryset(self):
        return Task.objects.filter(assignees=self.request.user)


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_manager:task-list")


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    context_object_name = "worker_list"

