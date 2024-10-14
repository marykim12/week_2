from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

class Photo(models.Model):
    TAG_CATEGORY = [
        ('nature', 'nature'),
        ('art', 'art'),
        ('scenery', 'scenery'),
        ('landscape', 'landscape')
    ]

    
    image = CloudinaryField('image')
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True) 
    likes = models.ManyToManyField('auth.User', related_name='liked_photos', blank=True)
    tag_category = models.CharField(max_length=40,choices=TAG_CATEGORY,default='nature')
    

def __str__(self):
    return self.title