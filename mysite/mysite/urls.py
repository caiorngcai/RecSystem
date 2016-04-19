"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from InfoRec import views as InfoRec_views

urlpatterns = [

    url(r'^$', InfoRec_views.home, name="home"),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^info/$', InfoRec_views.info, name="info"),
    # url(r'^info/(?P<article_id>)/$', InfoRec_views.article, name="article"),
    
    url(r'^partner/$', InfoRec_views.partner, name="partner"),
    # url(r'^partner/(?P<user_id>)/$', InfoRec_views.user, name="user"),

    # url(r'^tutor/$', InfoRec_views. name="tutor"),
    # url(r'^tutor/(?P<>)$', InfoRec_views. name=""),

    # url(r'^register/$', InfoRec_views.register, name="register"),
    url(r'^login/$', InfoRec_views.login, name="login"),
    url(r'^logout/$', InfoRec_views.logout, name="logout"),
]
