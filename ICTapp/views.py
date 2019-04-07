from django.shortcuts import render, get_object_or_404
from .models import Information
from django.views.generic import View
from .models import Specialty


def home(request):
   return render(request, 'ICTapp/index.html')


def informations(request):
   informations = Information.objects.all()
   return render(request, 'ICTapp/informations.html', context={'informations': informations})

class InformationDetailView(View):
   def get(self, request, pk):
      information = get_object_or_404(Information, pk=pk)
      return render(request, 'ICTapp/information_detail.html', context={'information': information})



class SpecialtyView(View):
   def get(self, request):
      specialty = Specialty.objects.all()
      return render(request, 'ICTapp/Specialty.html', context={
         'specialty': specialty,
      })


class SpecialtyDetailView(View):
   def get(self, request, slug):
      speciality = get_object_or_404(Specialty, slug=slug)
      return render(request, 'ICTapp/specialty_detail.html', context={'speciality': speciality})


class StaffView(View):
   def get(self, request):
      return render(request, 'ICTapp/staff.html')
