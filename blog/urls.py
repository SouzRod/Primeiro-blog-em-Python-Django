from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/(?P<pk>[0-9]+)$', views.post_detail, name='post_detail'),
    path('post/new/$', views.post_new, name='post_new'),
    path('post/(?P<pk>\d+)/edit/', views.post_edit, name='post_edit'),
]