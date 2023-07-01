from django.db import models
from datetime import date, timedelta

from mahalla import models as model

from mahalla.models import *
import datetime as dt
import calendar

class PeopleQuerySet(models.QuerySet):
    

    def check_deadline_taks(self,user,id):
        objects_list = model.People.objects.prefetch_related('id_categor').filter(id_categor__id=id,people__id_user=user)
        lists = []
        for i in objects_list:
            get_task = model.Tasks.objects.prefetch_related('id_people').filter(id_people = i.id)
            

        
        return True



class PeopleManager(models.Manager):
    
    def get_queryset(self):
        return PeopleQuerySet(self.model, using=self._db)
    
    def check_deadline_taks(self,user,id):
        return self.get_queryset().check_deadline_taks(user,id)