"""urls.py: Urls definidas."""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

# from app.views.DashboardView import DashboardView
from app.views.DashboardView import *

__author__ = "Caio Marinho"
__copyright__ = "Copyright 2019"

"""default URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/login/', auth_views.login),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^blog/$', BlogView.as_view(), name='blog'),
    url(r'^blog/categoria/(?P<categoria_id>\d+)/$', CategoriaView.as_view(), name='categoria'),
    url(r'^blog/(?P<post_id>\d+)/$', ViewPost.as_view(), name='post'),
    url(r'^blog/(?P<post_id>\d+)/confirm/$', ViewCapturaPlanilha.as_view(), name='captura_planilha'),
    url(r'^blog/(?P<post_id>\d+)/download/$', ViewPostDownload.as_view(), name='post_download'),
    url(r'^blog/(?P<slug>[-\w]+)/$', ViewPost.as_view(), name='post_slug'),
    url(r'^infograficos/$', InfograficoView.as_view(), name='infograficos'),
    url(r'^videos/$', VideoView.as_view(), name='videos'),
    url(r'^slides/$', SlideView.as_view(), name='slides'),
    url(r'^citacoes/$', CitacaoView.as_view(), name='citacoes'),
    url(r'^contato/$', ContactView.as_view(), name='contact'),

]
