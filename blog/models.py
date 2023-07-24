from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    post_title=models.CharField(max_length=100)
    post_content=models.TextField()
    post_date=models.DateTimeField(default=timezone.now)
    post_author=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.id})