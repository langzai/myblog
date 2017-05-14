from django.contrib import admin

# Register your models here.
from .models import Navigation,Category,Article

class NavigationAdmin(admin.ModelAdmin):
    list_display = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','navigation')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','category','pub_date','update_time')

admin.site.register(Navigation,NavigationAdmin)   
admin.site.register(Category,CategoryAdmin)   
admin.site.register(Article,ArticleAdmin)     