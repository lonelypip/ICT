from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   position = models.CharField(max_length=100, blank=True)
   information = models.TextField(blank=True)
   img = models.ImageField(default='default.jpg', upload_to='user_images')

   def __str__(self):
      return f'Профиль преподавателя {self.user.first_name} {self.user.last_name}'


   def get_absolute_url(self):
      return reverse('staff_detail_url', kwargs={'pk': self.pk})