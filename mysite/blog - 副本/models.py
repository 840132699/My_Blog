# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
class BlogType(models.Model):
    #博客类型    
    type_name = models.CharField(max_length=15)

class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    blog_type = models.ForeignKey(BlogType,on_delete=models.DO_NOTHING)
    created_time = models.DateField(auto_now_add=True)
    last_updated_time = models.DateField(auto_now_add=True)

