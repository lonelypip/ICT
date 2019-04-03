from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.core.exceptions import ValidationError



class UserUpdateForm(forms.ModelForm):
   email = forms.EmailField()

   class Meta:
      model = User
      fields = ('username','email')

   def clean_username(self):
      new_username = self.cleaned_data['username']
      print(new_username)
      if User.objects.filter(username=new_username).exists():
         raise ValidationError('Имя пользователя {} уже существует.'.format(new_username))
      return new_username


class ProfileImage(forms.ModelForm):
   def __init__(self, *args, **kwargs):
      super(ProfileImage, self).__init__(*args, **kwargs)
      self.fields['img'].label = "Изображение профиля"
      
   class Meta:
      model = Profile
      fields = ('img',)