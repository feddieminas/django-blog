from django.db import models
from django.utils import timezone

class Post(models.Model):
    """
    A single Blog post
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True) 
    # auto_now_add means as soon as record is created, then current date and time will be added to that field
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now) 
    # starts off with blank, nulls are allowed, default value is current time want to get from timezone
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True) # img uploads is the media folder one, NOT static
    
    def __unicode__(self):
        return self.title