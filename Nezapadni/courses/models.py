# courses/models.py
from django.db import models
from django.utils.text import slugify

class Course(models.Model):
    title = models.CharField(max_length=200)              
    slug = models.SlugField(max_length=200, unique=True)     
    description = models.TextField()                          
    image = models.ImageField(upload_to='courses/', blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)     

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
