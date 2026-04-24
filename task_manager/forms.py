from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from task_manager.models import Task, TaskType
import datetime


class TaskForm(forms.ModelForm):
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple(),
    )

    class Meta:
        model = Task
        fields = [
            "name",
            "description",
            "deadline",
            "priority",
            "task_type",
            "assignees"]
        widgets = {"deadline":
                   forms.DateInput(attrs={"type": "date",
                                          "class": "custom-date form-control",
                                          }
                                   )
                   }

    def clean_deadline(self):
        deadline = self.cleaned_data["deadline"]
        if deadline < datetime.date.today():
            raise ValidationError("Deadline date cannot be in the past"
                                  "")
        return deadline


class TaskTypeCreateForm(forms.ModelForm):
    class Meta:
        model = TaskType
        fields = "__all__"


class WorkerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username"}),)


class TaskSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"}),)


class WorkerForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ("position",)


class WorkerPositionUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["position"]
