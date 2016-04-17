from django.shortcuts import render
from django.http import HttpResponse
from InfoRec.models import User, Article
from django import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  #分页需要添加包

# Create your views here.

def home(request):
    post_list = Article.objects.all()[0:3]
    return render(request, 'home.html', {'post_list':post_list,})

def info(request):
    posts = Article.objects.all()[::-1]
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'info.html', {'post_list':post_list, 'rec_list':posts[0:10]});

def partner(request):
    user_list = User.objects.all()
    return render(request, 'partner.html', {'user_list':user_list});

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

# def register(request):
    # return render(request, 'register.html');
    
