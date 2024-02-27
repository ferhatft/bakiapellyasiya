from django.db import models
from django.db.models.fields import TextField
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class ClientopinionModel(models.Model):    
    title                           = models.CharField(max_length=40,verbose_name = "Client name",blank=True)
    company                         = models.CharField(max_length=40,verbose_name = "Şirket",blank=True)
    decription                      = models.TextField(max_length=400,verbose_name="Açıklama")
    decription_en                      = models.TextField(max_length=400,verbose_name="Açıklama_en",blank=True,null=True)


    def __str__(self):
        return '%s %s' % (self.title,self.id)

    
    def get_absolute_url(self):
        try:
            if self.slug:
                return "/dictionary/detail/{str}/".format(str=self.slug)
        except:
            return "/dictionary/detail/{str}/".format(str=self.title.lower().replace('-',' '))

    class Meta:
        ordering = ['id']
        verbose_name = 'Yorum'
        verbose_name_plural = 'yorumlar'



# app/models.py

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField('Book name', max_length=100)
    author = models.ForeignKey(User, blank=True, null=True,on_delete=models.SET_NULL )
    author_email = models.EmailField('Author email', max_length=75, blank=True)
    imported = models.BooleanField(default=False)
    published = models.DateField('Published', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.name