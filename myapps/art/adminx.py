from django.contrib import admin

# Register your models here.
import xadmin
from xadmin import views

from art.models import Category,Art
#配置主题
class BaseSetting:
    enable_themes = True
    use_bootswatch = True

class GlobalSettings:
    site_title = '文章后台管理系统'
    site_footer = '@<span style="font-size color:blue;">千峰教育</span><a class="btn btn-danger">zzpython1802'
    menu_style = 'accordion'

    globals_search_models = [Art,Category]
    global_models_icon = {
        Art:'glyphicon glyphicon-book',
        Category:'fa fa-cloud',
    }

#配置模型的输出字段
class CategoryAdmin:

    list_display = ['name', 'add_time']#显示的字段
    search_fields = ['name'] #搜索字段

class ArtAdmin:
    list_display = ['title', 'author', 'content', 'publish_time', 'category']
    search_fields = ['title', 'category__name']
    list_per_page = 10 #每页显示的条数
    style_fields = {
        'content':'ueditor'
    }



xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)

xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Art, ArtAdmin)

