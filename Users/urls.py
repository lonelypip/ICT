from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import redirect_view, profile
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
   path('', redirect_view, name='redirect_view_url'),
   path('sign-in/', LoginView.as_view(template_name='Users/sign_in.html'), name='sign_in_url'),
   path('sign-out/', LogoutView.as_view(template_name='Users/sign_out.html'), name='sign_out_url'),
   path('profile/', profile, name='profile_url'),
]

