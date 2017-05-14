from django.shortcuts import render

# Create your views here.

from django.http  import HttpResponse
from .models import Article,Navigation,Category

def index(request):
    
    navigations = Navigation.objects.all()
    categorys = Category.objects.filter(navigation = '随笔')
    cate_selec = categorys[0].name
    articles = Article.objects.filter(category = cate_selec)
    return render(request,'blog/index.html',{'navigations':navigations,'categorys':categorys,'articles':articles,'cate_selec':cate_selec})
   

def navigation_detail(request,navigation_name):
    navigations = Navigation.objects.all()
    categorys = Category.objects.filter(navigation = navigation_name)
    cate_selec = categorys[0].name
    articles = Article.objects.filter(category = cate_selec)
    return render(request,'blog/index.html',{'navigations':navigations,'categorys':categorys,'articles':articles,'cate_selec':cate_selec})

   

def category_detail(request,navigation_name,category_name):
    navigations = Navigation.objects.all()
    cate_selec = category_name
    categorys = Category.objects.filter(navigation = navigation_name)
    articles = Article.objects.filter(category = cate_selec)
   
    return render(request,'blog/index.html',{'navigations':navigations,'categorys':categorys,'articles':articles,'cate_selec':cate_selec})

  

def article_detail(request,navigation_name,category_name,article_title):
    navigations = Navigation.objects.all()
    categorys = Category.objects.filter(navigation = navigation_name)
    cate_selec = category_name
    article = Article.objects.get(title = article_title)
    return render(request,'blog/article.html',{'navigations':navigations,'categorys':categorys,'article':article,'cate_selec':cate_selec})
