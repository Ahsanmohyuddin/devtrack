from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Project
from .forms import ProjectForm, RegisterForm, TaskForm, Task


@login_required
def home(request):

    projects = Project.objects.filter(
        user=request.user
    )

    total_projects = projects.count()

    total_tasks = 0
    completed_tasks = 0

    for project in projects:

        tasks = project.tasks.all()

        total_tasks += tasks.count()

        completed_tasks += tasks.filter(
            completed=True
        ).count()

    pending_tasks = total_tasks - completed_tasks

    return render(
        request,
        "core/home.html",
        {
            "projects": projects,
            "total_projects": total_projects,
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "pending_tasks": pending_tasks,
        }
    )


@login_required
def about(request):
    return render(
        request,
        "core/about.html"
    )


@login_required
def project_list(request):
    projects = Project.objects.filter(
        user=request.user
    )

    return render(
        request,
        "core/project_list.html",
        {
            "projects": projects
        }
    )


@login_required
def project_create(request):

    if request.method == "POST":

        form = ProjectForm(request.POST)

        if form.is_valid():

            project = form.save(commit=False)
            project.user = request.user
            project.save()

            return redirect("/projects/")

    else:
        form = ProjectForm()

    return render(
        request,
        "core/project_form.html",
        {
            "form": form
        }
    )


@login_required
def project_update(request, id):

    project = Project.objects.get(
        id=id,
        user=request.user
    )

    if request.method == "POST":

        form = ProjectForm(
            request.POST,
            instance=project
        )

        if form.is_valid():

            form.save()

            return redirect("/projects/")

    else:

        form = ProjectForm(
            instance=project
        )

    return render(
        request,
        "core/project_form.html",
        {
            "form": form
        }
    )


@login_required
def project_delete(request, id):

    project = Project.objects.get(
        id=id,
        user=request.user
    )

    if request.method == "POST":

        project.delete()

        return redirect("/projects/")

    return render(
        request,
        "core/project_confirm_delete.html",
        {
            "project": project
        }
    )


def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("/login/")

    else:

        form = RegisterForm()

    return render(
        request,
        "core/register.html",
        {
            "form": form
        }
    )


@login_required
def task_create(request, project_id):

    project = Project.objects.get(
        id=project_id,
        user=request.user
    )

    if request.method == "POST":

        form = TaskForm(request.POST)

        if form.is_valid():

            task = form.save(commit=False)

            task.project = project

            task.save()

            return redirect("/projects/")

    else:

        form = TaskForm()

    return render(
        request,
        "core/task_form.html",
        {
            "form": form,
            "project": project
        }
    )

@login_required
def task_update(request, id):

    task = Task.objects.get(
        id=id,
        project__user=request.user
    )

    if request.method == "POST":

        form = TaskForm(
            request.POST,
            instance=task
        )

        if form.is_valid():

            form.save()

            return redirect("/projects/")

    else:

        form = TaskForm(
            instance=task
        )

    return render(
        request,
        "core/task_form.html",
        {
            "form": form,
            "project": task.project
        }
    )

@login_required    
def task_delete(request, id):

    task = Task.objects.get(
        id=id,
        project__user=request.user
    )

    if request.method == "POST":

        task.delete()

        return redirect("/projects/")

    return render(
        request,
        "core/task_confirm_delete.html",
        {
            "task": task
        }
    )