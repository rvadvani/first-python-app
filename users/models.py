from django.db import models

# Create your models here.

class Technology(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    class Gender(models.TextChoices):
        MALE = "Male"
        FEMALE = "Female"
        OTHER = "Other"
    # emp_id = models.UUIDField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    gender = models.CharField(max_length=20, choices=Gender, default=Gender.MALE)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=200)
    date_of_join = models.DateField("Date Of Join")
    technologies = models.ManyToManyField(Technology)
    photo = models.ImageField(upload_to="uploads", null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstName + " " + self.lastName


class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary = models.CharField(max_length=100)
    credit_on = models.DateField("Date Of Salary Credited")
    created_at = models.DateTimeField(auto_now=True)