from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   title = models.CharField(max_length=100)
   text = models.TextField()
   img = models.ImageField(upload_to='posts_images', blank=True)
   date = models.DateTimeField(default=timezone.now)

   def __str__(self):
      return self.title
   
   def get_absolute_url(self):
      return reverse('news_detail_url', kwargs={'pk':self.pk})
