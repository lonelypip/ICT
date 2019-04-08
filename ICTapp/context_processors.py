from .forms import QuestionForm

def question_form(request):
   return {'question_form': QuestionForm()}