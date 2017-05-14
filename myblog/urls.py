"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import include,url
from django.contrib import admin
from DjangoUeditor import urls as DjangoUeditor_urls
from blog import views as blog_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/', include(DjangoUeditor_urls)),
    url(r'^$',blog_views.index, name = 'index'),
    url(r'^navigation/(?P<navigation_name>[^/]+)/$',blog_views.navigation_detail,name= 'navigation'),
    url(r'^category/(?P<navigation_name>[^/]+)/(?P<category_name>[^/]+)/$',blog_views.category_detail,name= 'category'),
    url(r'^article/(?P<navigation_name>[^/]+)/(?P<category_name>[^/]+)/(?P<article_title>[^/]+)/$',blog_views.article_detail,name= 'article'),
    url(r'.*',blog_views.other)
]
