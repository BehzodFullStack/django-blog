from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    content = models.TextField(verbose_name="Maqola matni")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Oxirgi yangilanish sanasi")

    def __str__(self):
        return self.title
