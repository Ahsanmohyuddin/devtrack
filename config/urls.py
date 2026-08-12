"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from core.views import (
    home,
    about,
    project_list,
    project_create,
    project_update,
    project_delete,
    register,
    task_create,
    task_update,
    task_delete,
)


urlpatterns = [

    path(
        "admin/",
        admin.site.urls
    ),

    path(
        "",
        home,
        name="home"
    ),

    path(
        "about/",
        about,
        name="about"
    ),

    path(
        "projects/",
        project_list,
        name="project_list"
    ),

    path(
        "projects/add/",
        project_create,
        name="project_create"
    ),

    path(
        "projects/<int:id>/edit/",
        project_update,
        name="project_update"
    ),

    path(
        "projects/<int:id>/delete/",
        project_delete,
        name="project_delete"
    ),

    path(
        "register/",
        register,
        name="register"
    ),

    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="core/login.html"
        ),
        name="login"
    ),

    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout"
    ),

    path(
        "projects/<int:project_id>/tasks/add/",
        task_create,
        name="task_create"
    ),

    path(
    "tasks/<int:id>/edit/",
    task_update,
    name="task_update"
),

path(
    "tasks/<int:id>/delete/",
    task_delete,
    name="task_delete"
),

]

