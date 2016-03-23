from django.shortcuts import render
from django.http import HttpResponse
from InfoRec.models import User, Article
from django import forms

# Create your views here.

def home(request):
    post_list = Article.objects.all()[0:3]
    return render(request, 'home.html', {'post_list':post_list,})

# def login(request):
    # if request.method == "POST":
        # uf = UserForm(request.POST)
        # if uf.is_valid():
            # # 获取表单用户密码
            # username = uf.cleaned_data['username']
            # password = uf.cleaned_data['password']
            # # 获取表单数据与数据库进行比较
            # user = User.objects.filter(username_exact = username, password_exact = password)
            # if user:
                # return render(request, '')


