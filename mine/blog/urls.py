from django.conf.urls import url,include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^(?P<essay_id>\d+)$',views.details,name='details'),
    url(r'write/$',views.write,name='write'),
    url(r'save/$',views.save,name='save'),
    url(r'comment/$',views.comment,name='comment'),
    url(r'author/$',views.author,name='author'),
]