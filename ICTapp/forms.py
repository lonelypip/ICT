from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
   class Meta:
      model = Question
      fields = ('full_name', 'email', 'phone', 'text')

   def __init__(self, *args, **kwargs):
      super(QuestionForm, self).__init__(*args, **kwargs)
      self.fields['full_name'].label = "Имя Фамилия"
      self.fields['email'].label = "Эмэйл"
      self.fields['phone'].label = "Номер телефона"
      self.fields['text'].label = "Вопрос"