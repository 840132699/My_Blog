# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
class BlogType(models.Model):
    #博客类型    
    type_name = models.CharField(max_length=20)
    #定义显示的内容，不写的话只显示BlogTypeObjects
    def __str__(self):
        return self.type_name

class Blog(models.Model):
    title = models.CharField(max_length=50)
    blog_type = models.ForeignKey(BlogType,on_delete=models.DO_NOTHING)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateField(auto_now=True)

    def __str__(self):
        return "<Blog: %s>" %self.title