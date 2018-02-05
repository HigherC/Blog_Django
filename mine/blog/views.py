# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render,get_object_or_404,redirect
from django.http import JsonResponse
from models import *
import json
from .forms import NewEssay
# Create your views here.
def index(request):
    essay = Essay.objects.all()
    context = {'essay':essay}
    return render(request,'blog/index.html',context)

def details(request,essay_id):
    essay = get_object_or_404(Essay,id=essay_id)
    comment = Comment.objects.get(essay_id=essay_id)
    comment.read += 1
    context = {
        'essay_id':essay_id,
        'topic':essay.topic,
        'author':essay.author,
        'pub_date':essay.pub_date,
        'content':essay.content,
        'good':comment.good,
        'bad':comment.bad,
        'read':comment.read,
    }
    comment.save()
    return render(request,'blog/details.html',context)


def write(request):
    return render(request,'blog/write.html')

def save(request):
    form = NewEssay(request.POST)
    if form.is_valid():
        data = form.cleaned_data.copy()
        essay = Essay(topic=data['topic'],content=form.cleaned_data['content'],author=data['author'],pub_date=timezone.now())
        essay.save()
        essay.comment_set.create(read=0,good=0,bad=0,essay=essay)
        return redirect('index')
    else:
        return render(request,'blog/unfinished_essay.html')

#def save2(request):
#    topic = request.POST['topic']
#    content = request.POST['content']
#    author = request.POST['author']
#    pub_date = timezone.now()
#    essay = Essay(topic=topic,content=content,author=author,pub_date=pub_date)
#    essay.save()
#    essay.comment_set.create(read=0, good=0, bad=0, essay=essay)
    #comment = Comment(read=0, good=0, bad=0, essay=essay)
    #comment.save()
#    return redirect('/blog')

def comment(request):
    choice = request.POST['choice']
    essay_id = request.POST['essay_id']
    essay = get_object_or_404(Essay,id=essay_id)
    essay_comment = Comment.objects.get(essay_id=essay_id)
    if choice == 'good':
        essay_comment.good += 1
    else:
        essay_comment.bad += 1
    essay_comment.save()
    return redirect('index')

def author(request):
    return render(request,'blog/author.html')