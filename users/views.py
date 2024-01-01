from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


import json

usersData = open("/home/advani/Ramesh/Code/Practice/python/dashboard/users.json").read()
usersData = json.loads(usersData)


def index(request):
    data = {"fname": "Ramesh", "lname": "Advani"}
    return render(request, "users/index.html", data)


def users(request):
    return render(request, "users/users.html", usersData)

def details(request, user_id):
    users = usersData.get('users', [])
    singleUser = None
    for user in users:
        if 'id' in user and user['id'] == user_id:
            singleUser = user
            break

    return render(request, "users/details.html", {'user': singleUser})


def static(request):
    return HttpResponse("Hello, world. You're at the users index.")

