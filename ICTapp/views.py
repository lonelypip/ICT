from django.shortcuts import render, get_object_or_404
from .models import Information
from django.views.generic import View

def home(request):
   return render(request, 'ICTapp/index.html')


def informations(request):
   informations = Information.objects.all()
   return render(request, 'ICTapp/informations.html', context={'informations': informations})

class InformationDetailView(View):
   def get(self, request, pk):
      information = get_object_or_404(Information, pk=pk)
      return render(request, 'ICTapp/information_detail.html', context={'information': information})