from .forms import QuestionForm
from .models import Question
from django.shortcuts import redirect
from django.contrib import messages

def question_form(request):
   if request.method == 'POST':
      bound_form = QuestionForm(request.POST)
      if bound_form.is_valid():
         bound_form.save()
         messages.success(request, f'Ваш вопрос принят. Прошу ожидайте ответа')
   return {'question_form': QuestionForm()}


   
