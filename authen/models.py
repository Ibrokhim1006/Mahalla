from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Sektor(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=100)
    id_region = models.ForeignKey(Region,on_delete=models.CASCADE)
    id_sektor = models.ForeignKey(Sektor,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Mahalla(models.Model):
    name = models.CharField(max_length=250)
    id_sektor = models.ForeignKey(Sektor,on_delete=models.CASCADE)
    id_region = models.ForeignKey(Region,on_delete=models.CASCADE)
    id_districk = models.ForeignKey(District,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class CustumUsers(AbstractUser):
    phone = models.CharField(max_length=100,null=True,blank=True)
    position = models.CharField(max_length=250,null=True,blank=True)
    id_sektor = models.ForeignKey(Sektor,on_delete=models.CASCADE,null=True,blank=True)
    id_region = models.ForeignKey(Region,on_delete=models.CASCADE,null=True,blank=True)
    id_districk = models.ForeignKey(District,on_delete=models.CASCADE,null=True,blank=True)
    id_mahalla = models.ForeignKey(Mahalla,on_delete=models.CASCADE,null=True,blank=True)
    

