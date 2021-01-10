from django.db import models

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Yazar")
    # auth user dan kullanıcı adını alıyor.on delete ile de kullanıcı silinince makaleyi siliyor
    title = models.CharField(max_length=200, verbose_name="Başlık")
    content= models.TextField(verbose_name="İçerik")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturma zamanı")
    
    def __str__(self):
        return self.title
        # return self.author
    # makalenin başlığı ile gözükmesini sağlar
        
    
    