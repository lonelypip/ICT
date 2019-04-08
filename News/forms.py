from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
   class Meta:
      model = Comment
      fields = ('full_name', 'text')

   def __init__(self, *args, **kwargs):
      super(CommentForm, self).__init__(*args, **kwargs)
      self.fields['full_name'].label = "Имя Фамилия"
      self.fields['text'].label = "Текст"