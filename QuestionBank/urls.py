"""QuestionBank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from procfile import views as procfile_views
from contact import views as contact_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', procfile_views.home, name='home'),
    url(r'^about/', procfile_views.about, name='about'),
    url(r'^view_details1/', procfile_views.view_details_ban, name='ibps'),
    url(r'^aipmt/', procfile_views.aipmt, name='aipmt'),
    url(r'^ics/', procfile_views.ics, name='ics'),
    url(r'^banking/', procfile_views.banking, name='banking'),
    url(r'^current_affair/', procfile_views.current_affair, name='current_affair'),
    url(r'^motivation/', procfile_views.motivation, name='motivation'),
    url(r'^gk2017/', procfile_views.gk2017, name='gk2017'),
    url(r'^gk2016/', procfile_views.gk2016, name='gk2016'),
    url(r'^gk2015/', procfile_views.gk2015, name='gk2015'),
    url(r'^contact/', contact_views.contact, name='contact'),
    url(r'^fresh/', procfile_views.fresh, name='fresh'),
    url(r'^joining/', procfile_views.joining, name='joining'),
    url(r'^notification/', procfile_views.notification, name='notification'),

    url(r'^accounts/', include('allauth.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
