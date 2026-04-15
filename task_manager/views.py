from django.shortcuts import render

def index(request):
    """View function for the home page of the site."""

    return render(request, "task_manager/index.html", context={})