from django import forms
from .models import FileUpload

class UploadFilesForm(forms.Form):
    title = forms.CharField(max_length=200)
    file = forms.FileField()
    