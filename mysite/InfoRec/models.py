# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# 用户类
class myuser(models.Model):
    user = models.OneToOneField(User)
    # nickname = models.CharField(max_length=16)
    # attention = models.CharField(max_length=16)
    permission = models.IntegerField(default=1)

    def __str__(self):
        return self.user.username

# 文章类
class myarticle(models.Model):
    title = models.CharField(max_length=256)
    abstract = models.TextField(max_length=1000)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, editable=True)
    tag = models.CharField(max_length=256, blank=True)
    # update_time = models.DateTimeField("更新时间", auto_now=True, null=True)
    
    def __str__(self):
        return self.title

# 导师类
# class Tutor(model.Model):

# 信息推荐结果表
# class RecoArticle(models.Model):

# 伙伴推荐结果表
# class RecoPartner(models.Model):

# 导师推荐结果表
# class RecoTutor(models.Model):
