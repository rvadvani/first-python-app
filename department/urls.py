from django.urls import path

from . import views

urlpatterns = [
    path("/members", views.members, name="members"),
    path("", views.DepartmentsView.as_view(), name="departments"),
    path("<int:pk>/", views.DepartmentDetailView.as_view(), name="department.detail"),
]