#coding:utf-8
from django.db import models

# Create your models here.
from DjangoUeditor.models import UEditorField
from django.core.urlresolvers import reverse


class Navigation(models.Model) :
    name = models.CharField('导航条目', max_length = 256,primary_key=True)
    

    def get_absolute_url(self):
        return reverse('navigation',args = (self.name,))
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '导航栏目'
        verbose_name_plural = '导航栏目'


class Category(models.Model):
    name = models.CharField('类别',max_length = 256,primary_key=True)
    navigation = models.ForeignKey(Navigation,verbose_name='导航栏目')
    
    def get_absolute_url(self):
        return reverse('category',args = (self.navigation.name,self.name,))

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '类别'
        verbose_name_plural = '类别'

class Article(models.Model):
    title = models.CharField('标题', max_length = 256,primary_key=True)
    category = models.ForeignKey(Category,verbose_name='类别')
    introduction = UEditorField('简介', height=100, width=1000,default=u'', blank=True,toolbars='besttome', filePath='uploads/files/')
    content = UEditorField('内容', height=300, width=1000,default=u'', blank=True,toolbars='besttome',imagePath="uploads/images/", filePath='uploads/files/')
    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable = True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)

    def get_absolute_url(self):
        return reverse('article',args = (self.category.navigation,self.category.name,self.title))
   
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

