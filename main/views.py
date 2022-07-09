from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
from .forms import CreateNewList


def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response,"main/list.html",{"ls":ls})


def home(response):
        return render(response,"main/home.html",{})


def create(response):
        if response == "POST":
                form = CreateNewList()
                if form.is_valid():
                        n = form.cleaned_data["name"]
                        t =ToDoList(name=n)
                        t.save()
        else:
                form = CreateNewList()
        return render(response,"main/create.html",{"form": form})
