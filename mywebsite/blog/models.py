from django.db import models

# Create your models here.

from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
class AwardImageUpload(models.Model):
    title = models.CharField(max_length=30, null=True)
    image = models.ImageField(upload_to='about_me/awards/%Y/%m/%d', blank=True)
        
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
        
    def __str__(self):
        return f'{self.title}'
        