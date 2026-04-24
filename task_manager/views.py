from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from task_manager.forms import (
    TaskForm,
    WorkerForm,
    TaskTypeCreateForm,
    WorkerPositionUpdateForm,
    WorkerSearchForm,
    TaskSearchForm
)
from task_manager.models import Task, TaskType, Position


@login_required
def index(request):
    """View function for the home page of the site."""
    num_uncompleted_tasks = Task.objects.all().filter(
        is_completed=False
    ).count()
    num_completed_tasks = Task.objects.all().filter(
        is_completed=True
    ).count()
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
    return render(request, "account_info/account_info.html", context=context)


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

    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("name", "")
        context["search_name"] = TaskSearchForm(initial={"name": username})
        return context

    def get_queryset(self):
        queryset = Task.objects.filter(assignees=self.request.user)
        form = TaskSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_manager:task-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_manager:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task_manager:task-list")


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    template_name = "task_manager/task_type_form.html"
    form_class = TaskTypeCreateForm
    success_url = reverse_lazy("task_manager:task-create")


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    fields = "__all__"
    template_name = "task_manager/task_type_form.html"
    success_url = reverse_lazy("task_manager:task-type")


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    success_url = reverse_lazy("task_manager:task-type")


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    template_name = "task_manager/tasktyp_list.html"


class PositionCreateView(
    LoginRequiredMixin,
    generic.CreateView
):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("task_manager:worker-create")


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = get_user_model()
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_username"] = WorkerSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        queryset = get_user_model().objects.all()
        form = WorkerSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return queryset


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = get_user_model()
    form_class = WorkerForm


class WorkerPositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = get_user_model()
    form_class = WorkerPositionUpdateForm
    template_name = "task_manager/worker_form.html"
    success_url = reverse_lazy("task_manager:worker-list")
