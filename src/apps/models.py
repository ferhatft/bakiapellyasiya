from django.db import models
from django.db.models.fields import CharField

from django.template.defaultfilters import slugify

from ckeditor_uploader.fields import RichTextUploadingField




class İnstansiyaMahkemesiModel(models.Model):
    name                            = models.CharField(max_length=100,verbose_name='İsim')

    def __str__(self):
        return '%s %s' % (self.name, self.id)

    class Meta:
        ordering = ['id']
        verbose_name = '1-ci instansiya'
        verbose_name_plural = '1-ci instansiyalar'





class instansiyaMahkemesihakimiModel(models.Model):
    name                            = models.CharField(max_length=100,verbose_name='İsim')

    def __str__(self):
        return '%s %s' % (self.name, self.id)


    class Meta:
        ordering = ['id']
        verbose_name = '1-ci instansiya məhkəməsinin hakim'
        verbose_name_plural = '1-ci instansiya məhkəməsinin hakimləri'


class ikinciinstansiyaMahkemesihakimiModel(models.Model):
    name                            = models.CharField(max_length=100,verbose_name='İsim')

    def __str__(self):
        return '%s %s' % (self.name, self.id)


    class Meta:
        ordering = ['id']
        verbose_name = 'Apelyasiya məhkəməsi hakim'
        verbose_name_plural = 'Apelyasiya məhkəməsi hakimləri'

        