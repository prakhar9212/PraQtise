from django.conf.urls import url
from django.contrib import admin

from .views import (
    UserCreateAPIView,
    UserLoginAPIVIEW,
    )

urlpatterns = [
    url(r'^login$', UserLoginAPIVIEW.as_view(), name='login'),

    url(r'^register$', UserCreateAPIView.as_view(), name='register'),


]