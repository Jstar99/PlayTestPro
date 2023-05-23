from django.shortcuts import render, redirect
from .models import Project
from .forms import UploadFilesForm

# Create your views here.

def project_upload(request):
   myProjects = Project.objects.all().values() 
   return render(request, 'devSide/uploadPage.html')


















   #i f(request.method == 'POST'):
    #         form = UploadFolderForm(request.POST, request.FILES)
    #         if(form.is_valid):
    #             form.save()
    #             return redirect('upload_folder_success')
    #         else:
    #             form = UploadFolderForm()
    #return render(request, 'devSide/uploadPage.html', {'form', form}) 