# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Essay(models.Model):
    topic = models.CharField(max_length=256)
    content = models.TextField()
    author = models.CharField(max_length=64)
    pub_date = models.DateTimeField('date_published')
    def __str__(self):
        return self.topic

class Comment(models.Model):
    essay = models.ForeignKey(Essay)
    read = models.IntegerField()
    #点赞的
    good = models.IntegerField()
    #踩的
    bad = models.IntegerField()