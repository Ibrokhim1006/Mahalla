from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from authen.forms import *
from authen.models import *

admin.site.register(Sektor)
admin.site.register(Region)
admin.site.register(District)
admin.site.register(Mahalla)

class NewMyUser(UserAdmin):
    add_form = CreasteUser
    form = ChangeUser
    model = CustumUsers
    list_display = ['username','first_name','last_name','id',]
    fieldsets = UserAdmin.fieldsets + (
        (None,{'fields':('phone','id_sektor','id_region','id_districk','id_mahalla','position',)}),
    )
    add_fieldsets = (
        (None,{'fields':('username','password1','password2')}),
    )
admin.site.register(CustumUsers,NewMyUser)
