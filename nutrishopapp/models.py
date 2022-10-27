from os import link
from django.db import models
from distutils.command.upload import upload
from django.db import models
from datetime import datetime
from turtle import title
from django.forms import DateTimeField
from django.contrib.auth.models import User
# Create your models here.


class Blog(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField(blank=True)
    body2=models.TextField(blank=True)
    image = models.ImageField(upload_to = 'blog_image', blank=True , null=True)
    

    def __str__(self):
        return self.title
    class Meta:
        ordering=['-id']


class Trending(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField(blank=True)
    image = models.ImageField(upload_to = 'blog_image', blank=True , null=True)
    Link=models.URLField(max_length=200)

    def __str__(self):
        return self.title
    class Meta:
        ordering=['-id']

class Popular(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField(blank=True)
    image = models.ImageField(upload_to = 'blog_image', blank=True , null=True)
    Link=models.URLField(max_length=200)

    image2 = models.ImageField(upload_to = 'blog_image', blank=True , null=True)
    Link2=models.URLField(max_length=200)
    title2=models.CharField(max_length=200)
    body2=models.TextField(blank=True)

    image3 = models.ImageField(upload_to = 'blog_image', blank=True , null=True)
    Link3=models.URLField(max_length=200)
    title3=models.CharField(max_length=200)
    body3=models.TextField(blank=True)

    image4 = models.ImageField(upload_to = 'blog_image', blank=True , null=True)
    Link4=models.URLField(max_length=200)
    title4=models.CharField(max_length=200)
    body4=models.TextField(blank=True)
   

    def __str__(self):
        return self.title
    class Meta:
        ordering=['-id']

class Newrelease(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField(blank=True)
    image = models.ImageField(upload_to = 'blog_image', blank=True , null=True)
    Link=models.URLField(max_length=200)

    image2 = models.ImageField(upload_to = 'blog_image', blank=True , null=True)
    Link2=models.URLField(max_length=200)
    title2=models.CharField(max_length=200)
    body2=models.TextField(blank=True)

    image3 = models.ImageField(upload_to = 'blog_image', blank=True , null=True)
    Link3=models.URLField(max_length=200)
    title3=models.CharField(max_length=200)
    body3=models.TextField(blank=True)

    image4 = models.ImageField(upload_to = 'blog_image', blank=True , null=True)
    Link4=models.URLField(max_length=200)
    title4=models.CharField(max_length=200)
    body4=models.TextField(blank=True)
   

    def __str__(self):
        return self.title
    class Meta:
        ordering=['-id']

class Sleep(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField(blank=True)
    image = models.ImageField(upload_to = 'blog_image', blank=True , null=True)
    Link=models.URLField(max_length=200)

    image2 = models.ImageField(upload_to = 'blog_image', blank=True , null=True)
    Link2=models.URLField(max_length=200)
    title2=models.CharField(max_length=200)
    body2=models.TextField(blank=True)

    image3 = models.ImageField(upload_to = 'blog_image', blank=True , null=True)
    Link3=models.URLField(max_length=200)
    title3=models.CharField(max_length=200)
    body3=models.TextField(blank=True)

    image4 = models.ImageField(upload_to = 'blog_image', blank=True , null=True)
    Link4=models.URLField(max_length=200)
    title4=models.CharField(max_length=200)
    body4=models.TextField(blank=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering=['-id']

class Protein(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField(blank=True)
    image = models.ImageField(upload_to = 'blog_image', blank=True , null=True)
    Link=models.URLField(max_length=200)

    image2 = models.ImageField(upload_to = 'blog_image', blank=True , null=True)
    Link2=models.URLField(max_length=200)
    title2=models.CharField(max_length=200)
    body2=models.TextField(blank=True)

    image3 = models.ImageField(upload_to = 'blog_image', blank=True , null=True)
    Link3=models.URLField(max_length=200)
    title3=models.CharField(max_length=200)
    body3=models.TextField(blank=True)

    image4 = models.ImageField(upload_to = 'blog_image', blank=True , null=True)
    Link4=models.URLField(max_length=200)
    title4=models.CharField(max_length=200)
    body4=models.TextField(blank=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering=['-id']


