from django.contrib import admin
from InfoRec.models import User, Article 

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'password', 'email')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title','pub_date','tag')

admin.site.register(User, UserAdmin)
admin.site.register(Article, ArticleAdmin)
