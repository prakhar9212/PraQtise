from django.conf.urls import url
from django.contrib import admin



from .views import (
    PostCreateAPIView,
    PostDetailAPIView,
    PostListAPIView,
    PostDeleteAPIView,
    PostUpdateAPIView
    )

urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name='list'),
    url(r'^create/$', PostCreateAPIView.as_view()),
    url(r'^(?P<pk>\d+)/$', PostDetailAPIView.as_view(), name='detail'),
     url(r'^(?P<pk>\d+)/edit/$',PostUpdateAPIView.as_view() , name='update'),
    url(r'^(?P<pk>\d+)/delete/$',PostDeleteAPIView.as_view(),name='delete'),
]