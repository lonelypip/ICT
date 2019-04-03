from django.db import models
from django.utils import timezone
from django.urls import reverse



class Information(models.Model):
   title = models.CharField(max_length=100)
   text = models.TextField()
   location = models.CharField(max_length=100)
   img_main = models.ImageField(upload_to='posts_images', blank=True)
   img_1 = models.ImageField(upload_to='event_images', blank=True)
   img_2 = models.ImageField(upload_to='event_images', blank=True)
   img_3 = models.ImageField(upload_to='event_images', blank=True)
   date = models.DateTimeField(default=timezone.now)

   def __str__(self):
      return self.title
   
   def get_absolute_url(self):
      return reverse('information_detail_url', kwargs={'pk':self.pk})