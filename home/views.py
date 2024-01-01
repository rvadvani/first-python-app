from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

from users.models import Employee, Department
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

# Create your views here.
@login_required(login_url="/login/")
def home(request):
    # department = Department(name="Development")
    # department.save()
    # department = Employee(department_id=1, firstName="Vikram", lastName="Aditya", gender="Male", email="vikram@aditya.io", phone="+919008890808", address="Whitefield", city="Bengaluru", date_of_join="2045-09-17")
    # department.save()
    employees = Employee.objects.all()
    context = {"employees": employees}
    return render(request, "home/index.html", context)

def create(request):
    departments = Department.objects.all()
    context = {"departments": departments}
    return render(request, "home/create.html", context)

def edit(request, id):
    try:
        employee = Employee.objects.get(pk=id)
        # Or you can try with this method also from django.shortcute import get_object_or_404
        # member = get_object_or_404(Employee, pk=id)
    except Employee.DoesNotExist:
        raise Http404("Employee does not exist")

    context = {"employee": employee}
    return render(request, "home/edit.html", context)

def store(request):
    emp = request.POST

    photo = request.FILES['photo']
    fs = FileSystemStorage()
    photo_name = fs.save(photo.name, photo)

    employee = Employee(
        department_id=emp['department_id'],
        firstName=emp['firstName'],
        lastName=emp['lastName'],
        gender=emp['gender'],
        email=emp['email'],
        phone=emp['phone'],
        address=emp['address'],
        city=emp['city'],
        date_of_join=emp['date_of_join'],
        photo=fs.url(photo_name)
    )
    employee.save()
    # print(request.POST["department_id"])
    return redirect("/employee/create/")

class EmployeeDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/login/'
    # Employee.technologies.add(1)
    model = Employee
    template_name = "home/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['salaries'] = context['employee'].salary_set.all().order_by('-credit_on')
        queryset = context['employee'].technologies.all()
        technology_names = [technology.name for technology in queryset]
        context['technologies'] = ', '.join(technology_names)
        return context
