from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from task_manager.models import Position, Task, Worker


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    pass
