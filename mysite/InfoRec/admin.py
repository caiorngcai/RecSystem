from django.contrib import admin
from .models import User, Article 

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','tag')

admin.site.register(User, UserAdmin)
admin.site.register(Article, ArticleAdmin)
