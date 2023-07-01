from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from authen.models import *
from mahalla.managers import *


class Categoriya(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name
    
class People(models.Model):
    full_name = models.CharField(max_length=150)
    birth_date = models.DateField()
    phone = models.CharField(max_length=100)
    village = models.CharField(max_length=250)
    additional_information = RichTextUploadingField()
    id_categor = models.ForeignKey(Categoriya,on_delete=models.CASCADE)
    id_mahalla = models.ForeignKey(Mahalla,on_delete=models.CASCADE,null=True,blank=True)
    id_sektor =  models.ForeignKey(Sektor,on_delete=models.CASCADE,null=True,blank=True)
    id_region = models.ForeignKey(Region,on_delete=models.CASCADE,null=True,blank=True)
    id_districk = models.ForeignKey(District,on_delete=models.CASCADE,null=True,blank=True)
    responsible_employee = models.ForeignKey(CustumUsers,on_delete=models.CASCADE ,blank=True,null=True,related_name='responsible_employee')
    create_user = models.ForeignKey(CustumUsers,on_delete=models.CASCADE,blank=True,null=True,related_name='create_user')
    create_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.full_name
    
class TaskCategoriya(models.Model):
    name = models.CharField(max_length=100)
    date = models.SmallIntegerField()
    def __str__(self):
        return self.name

class Tasks(models.Model):
    id_people = models.ForeignKey(People,on_delete=models.CASCADE,null=True,blank=True,related_name='people')
    id_task_category = models.ForeignKey(TaskCategoriya,on_delete=models.CASCADE)
    id_user = models.ForeignKey(CustumUsers,on_delete=models.CASCADE,related_name='id_user')
    task = RichTextUploadingField()
    is_user = models.BooleanField(default=False,null=True,blank=True)
    is_task = models.BooleanField(default=False,null=True,blank=True)
    files =  models.FileField(upload_to='doc/',null=True,blank=True)
    comment = models.TextField(max_length=250,null=True,blank=True)
    create_date = models.DateField(auto_now_add=True)
    date_line = models.DateField(null=True,blank=True)

    objects =  PeopleManager()   

class Performance(models.Model):
    id_task = models.ManyToManyField(Tasks)
    id_user = models.ForeignKey(CustumUsers,on_delete=models.CASCADE)
    is_responsible_employee = models.BooleanField(default=False)
    is_task = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
