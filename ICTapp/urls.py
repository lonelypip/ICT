from django.urls import path
from .views import home, informations, InformationDetailView, SpecialtyView, SpecialtyDetailView, StaffView, StaffDetailView


urlpatterns = [
   path('', home, name='home_url'),
   path('student-life/', informations, name='informations_url'),
   path('student-life/<int:pk>/', InformationDetailView.as_view(), name='information_detail_url'),
   path('specialty/', SpecialtyView.as_view(), name='specialty_url'),
   path('specialty/<str:slug>/', SpecialtyDetailView.as_view(), name='specialty_detail_url'),
   path('staff/', StaffView.as_view(), name='staff_url'),
   path('staff/<int:pk>/', StaffDetailView.as_view(), name='staff_detail_url')
]