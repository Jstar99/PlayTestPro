from django.db import models

class FileUpload(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='')

class Project(models.Model):
    project_file = models.FileField(upload_to='static/')
    project_screenshot = models.FileField(upload_to='media/')
    project_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    project_details = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')
    user_num = models.IntegerField(default=0)
    max_user_num = models.IntegerField(default=0)
    tier = models.CharField(max_length=20, default="")
    
    def __str__(self):
        return self.project_name
