from django.urls import path
from .views import ShowNewsView, NewsDetailView, CreateNewsView, UpdateNewsView, DeleteNewsView


urlpatterns = [
   path('', ShowNewsView.as_view(), name='news_url'),
   path('post/<int:pk>/', NewsDetailView.as_view(), name='news_detail_url'),
   path('post/add/', CreateNewsView.as_view(), name='news_add_url'),
   path('post/<int:pk>/update/', UpdateNewsView.as_view(), name='news_update_url'),
   path('post/<int:pk>/delete/', DeleteNewsView.as_view(), name="news_delete_url"),
]

