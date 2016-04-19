from django.contrib import admin
from InfoRec.models import myuser, myarticle 

# Register your models here.

class myuserAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'password', 'email')

class myarticleAdmin(admin.ModelAdmin):
    list_display = ('id','title','pub_date','tag')

admin.site.register(myuser, myuserAdmin)
admin.site.register(myarticle, myarticleAdmin)
