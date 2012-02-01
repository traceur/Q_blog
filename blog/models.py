from django.db import models

# Create your models here.

class post(models.Model):
    title = models.CharField(max_length=200,verbose_name='Post_title')
    value = models.TextField(verbose_name='Post_value')
    time = models.DateTimeField(auto_now_add=True, verbose_name='Time')
    tag = models.CharField(max_length=200, verbose_name='Post_tag')

    def __unicode__(self):
        return self.title

class link(models.Model):
    title = models.CharField(max_length=200,verbose_name='Link_title')
    link = models.CharField(max_length=200,verbose_name='Link_value')

    def __unicode__(self):
        return self.title

