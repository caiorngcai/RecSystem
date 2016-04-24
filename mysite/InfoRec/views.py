from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  #分页需要添加包
from django.core.urlresolvers import reverse
from InfoRec.models import myuser, myarticle
from django import forms

# Create your views here.

def home(request):
    user = request.user if request.user.is_authenticated() else None
    post_list = myarticle.objects.all()[0:3]

    content={
        'post_list':post_list,
        'user':user,
    }
    return render(request, 'home.html', content)

def info(request):
    user = request.user if request.user.is_authenticated() else None

    posts = myarticle.objects.all()[::-1]
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.paginator(paginator.num_pages)

    content = {
        'post_list':post_list,
        'rec_list':posts[0:10],
        'user':user,
    }
    return render(request, 'info.html', content);

# def info_detail(request, articleId):
    # return HttpResponse("Hello World!")

def partner(request):
    user = request.user if request.user.is_authenticated() else None
    print(user)

    user_list = myuser.objects.all()

    content={
        'user_list':user_list,
        'user':user,
    }
    return render(request, 'partner.html', content);

def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse("home"))
    state = None
    if request.method == "POST":

        username = request.POST.get('username','')
        password = request.POST.get('password','')
        password_repeat = request.POST.get('password_repeat','')
        email_address = request.POST.get('email','')

        if password=='' or password_repeat=='' :
            state='empty'
        elif password != password_repeat:
            state='repeat_error'
        elif User.objects.filter(username=username):
            state='user_exist'
        else:
            new_user = User.objects.create_user(username=username, password=password, email=email_address)
            new_user.save()
            new_myuser = myuser(user=new_user,)
            new_myuser.save()
            state='success'

    content = {
        'active_menu': 'home',
        'state': state,
        'user': None,
    }
    return render(request, 'register.html', content)

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home'))
    state = None
    if request.method == "POST":
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            state = 'not_exist_or_password_error'
    
    content={
        'state': state,
        'user': None
    }
    return render(request, 'login.html', content);
    

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))
