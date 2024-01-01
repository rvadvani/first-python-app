from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.create, name="employee.create"),
    path("store/", views.store, name="employee.store"),
    path("<int:id>/edit/", views.edit, name="employee.edit"),
    path("<int:pk>/view/", views.EmployeeDetailView.as_view(), name="employee.view"),
]