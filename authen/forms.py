from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from authen.models import *

class CreasteUser(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustumUsers
        fields = ('username','first_name','last_name','phone','id_sektor','id_region','id_districk','id_mahalla','position','password')


class ChangeUser(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustumUsers
        fields = ('username','first_name','last_name','phone','id_sektor','id_region','id_districk','id_mahalla','position','password')