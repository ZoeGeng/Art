from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50,verbose_name='分类名')
    add_time = models.DateTimeField(verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_cate'
        verbose_name = '分类表'
        verbose_name_plural = verbose_name

class Art(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name='标题')
    summary = models.CharField(max_length=200,
                               verbose_name='简介')
    # content = models.TextField(verbose_name='内容',
    #                            null=True)
    content = UEditorField(verbose_name='内容',
                           width=640,height=480,
                           imagePath='art/u_images/',
                           filePath='art/u_files/',
                           toolbars='full',
                           blank=True,
                           null=True)
    author = models.CharField(max_length=50,
                              verbose_name='作者')
    publish_time = models.DateTimeField(verbose_name='发布时间',
                                        auto_now_add=True)

    category = models.ForeignKey(Category,
                                 related_name='arts',
                                 on_delete=models.CASCADE,
                                 verbose_name='分类')
    #upload_to指定图片路径是相对于MEDIA_ROOT
    cover = models.ImageField(verbose_name='封面',
                              upload_to='art/images/',
                              null=True)


    def __str__(self):
        return self.title

    @property
    def shortTitle(self):
        if len(self.title) > 8:
            return self.title[0:8] + ".."
        return self.title

    class Meta:
        db_table = 't_art'
        verbose_name = '文章表'
        verbose_name_plural = verbose_name