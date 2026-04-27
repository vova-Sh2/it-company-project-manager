from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
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


USER = get_user_model()


class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = "task_manager/index.html"


class AccountInfoView(LoginRequiredMixin, generic.TemplateView):
    template_name = "account_info/account_info.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["completed_tasks"] = Task.objects.filter(
            is_completed=True
        ).count()

        return context


class TaskCompleteView(LoginRequiredMixin, generic.View):

    def post(self, request, pk):
        Task.objects.filter(id=pk).update(is_completed=True)

        return redirect(request.GET.get("next","/"))


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
    model = USER
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_username"] = WorkerSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        queryset = USER.objects.all()
        form = WorkerSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return queryset


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = USER
    form_class = WorkerForm


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = USER
    template_name = "task_manager/worker_confirm_delete.html"
    success_url = reverse_lazy("task_manager:worker-list")



class WorkerPositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = USER
    form_class = WorkerPositionUpdateForm
    template_name = "task_manager/worker_form.html"
    success_url = reverse_lazy("task_manager:worker-list")
