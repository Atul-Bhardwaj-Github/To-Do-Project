from django.shortcuts import render,redirect
from .forms import *

from .models import *

from django.core.paginator import Paginator


# Create your views here.

def home(request):
    AllData=List.objects.all()
    paginator=Paginator(AllData,2)
    page_number=request.GET.get("page")
    ListData = paginator.get_page(page_number)
    context={
        "ListData":ListData
    }
    return render(request,"index.html",context)

def addItem(request):
    if request.method=="POST":
        Title=request.POST.get("Title")
        Detail=request.POST.get("Detail")
        Item=List(Title=Title,Detail=Detail)

        Item.save()

        return redirect("/")
    form=List_form()
    context={
        "form":form
    }
    return render(request,"addItem.html",context)

def edit(request,id):
    if request.method=="POST":
        Item=List.objects.get(id=id)
        Item.Title=request.POST.get("Title")
        Item.Detail=request.POST.get("Detail")
        
        Item.save()
        return redirect("/")
    form=List_form(id)
    context={
        "form":form
    }
    return render(request,"edit.html",context)

def delete_Item(request,id):
    Item=List.objects.get(id=id)
    Item.delete()
    return redirect("/")