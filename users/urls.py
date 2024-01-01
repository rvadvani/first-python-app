from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="users"),
    path("users/", views.users, name="users.data"),
    path("details/<int:user_id>/", views.details, name="user.detail"),
    path("static/", views.static, name="static"),
]