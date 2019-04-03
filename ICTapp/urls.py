from django.urls import path
from .views import home, informations, InformationDetailView


urlpatterns = [
   path('', home, name='home_url'),
   path('student-life/', informations, name='informations_url'),
   path('student-life/<int:pk>/', InformationDetailView.as_view(), name='information_detail_url')
]