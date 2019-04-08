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


class Specialty(models.Model):
   name = models.CharField(max_length=100)
   slug = models.SlugField()
   description = models.TextField()
   purpose = models.TextField()
   tasks = models.TextField()
   perspectives = models.TextField()
   img = models.ImageField(upload_to='Specialty_images', blank=True)

   def __str__(self):
      return self.name
   
   def get_absolute_url(self):
      return reverse('specialty_detail_url', kwargs={'slug':self.slug})


class Discipline(models.Model):
   specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="disciplines")
   name = models.CharField(max_length=100)

   def __str__(self):
      return self.name



class Question(models.Model):
   full_name = models.CharField(max_length=50)
   email = models.EmailField()
   phone = models.IntegerField()
   text = models.TextField()

   def __str__(self):
      return self.text