from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from InfoRec.models import myuser, myarticle 
from InfoRec.models import *

# Register your models here.

class myuserInline(admin.StackedInline):
    model = myuser
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = (myuserInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# class myuserAdmin(admin.ModelAdmin):
    # model = myuser
    # list_display = ('id','username', 'password', 'email')

class myarticleAdmin(admin.ModelAdmin):
    list_display = ('id','title','pub_date','tag')

# admin.site.register(myuser, myuserAdmin)
admin.site.register(myarticle, myarticleAdmin)
