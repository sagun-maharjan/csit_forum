"""forum URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home,name="home"),
    url(r'^dashboard$',views.dashboard,name='dashboard'),
    url(r'^question',views.question,name='question'),
    url(r'^syllabus/$',views.syllabus,name='syllabus'),
    url(r'^syllabus_detail/(?P<id>[0-9]+)', views.syllabus_detail, name='syllabus_detail')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
