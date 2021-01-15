
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Yazar")
    # auth user dan kullanıcı adını alıyor.on delete ile de kullanıcı silinince makaleyi siliyor
    title = models.CharField(max_length=200, verbose_name="Başlık")
    # content= models.TextField(verbose_name="İçerik")
    content= RichTextField(verbose_name="İçerik")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturma zamanı")
    article_image = models.FileField(blank=True,null=True, verbose_name="Add an image")
    
    def __str__(self):
        return self.title
        # return self.author
    # makalenin başlığı ile gözükmesini sağlar
    
class Comment(models.Model):
    article=models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Comment", related_name="comment")
    comment_author = models.CharField(max_length=50, verbose_name="Author")
    comment_content = models.CharField(max_length=200, verbose_name="Content")
    comment_created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created time")
    
        
    
    