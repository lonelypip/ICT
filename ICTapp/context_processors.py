from .forms import QuestionForm
from .models import Question
from django.shortcuts import redirect

def question_form(request):
   return {'question_form': QuestionForm()}


   # full_name = request.POST.get('full_name')
   # email = bound_form.cleaned_data['email']
   # phone = bound_form.cleaned_data['phone']
   # text = bound_form.cleaned_data['text']
   # print(full_name)
   # # question = Question.objects.create(post=post, full_name=full_name, text=text)
   # # comment.save()
   # # messages.success(request, f'Ваш комментарий в рассмотрений')
   # return redirect('home_url')
