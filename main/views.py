from django.shortcuts import render
from devSide.models import Project
from django.apps import apps
from registration.models import MyUser
from django.contrib.auth.decorators import login_required


# Create your views here.

def Homepage(request):
    return render(request, "main/home.html",)

def ProjectsPage(request):
    project_list = Project.objects.order_by('-pub_date')
    return render(request, "main/projectPage.html",  {'project_list' : project_list})

@login_required
def PointsPage(request):
    
    return render(request,"userSide/pointsPage.html")


def ProjectEnnead(request):
    return render(request, "downloadPages/projectEnnead.html")












# def DownloadPage(request):
#     projects = Project.objects.all()
#     # model_class = apps.get_model("devSide", model_name=project_name)
#     # instances = model_class.objects.all()
#     # context = {'instances' : instances}
#     return render(request, "main/downloadPage.html", {'projects' : projects})