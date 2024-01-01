from django.shortcuts import render
from django.http import HttpResponse
from users.models import Employee, Department

# Create your views here.
from django.views import generic

def members(request):
    # return HttpResponse("Hello, world. You're at the users index.")
    return render(request, "department/index.html", {})



class DepartmentsView(generic.ListView):
    template_name = "department/index.html"
    # <app name>/<model name>_list.html default template eg. users/department_list.html
    context_object_name = "departments"
    # default object_name is module_list eg. department_list

    def get_queryset(self):
        return Department.objects.all()


class DepartmentDetailView(generic.DetailView):
    model = Department
    template_name = "department/detail.html"