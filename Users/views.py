from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileImage
from django.contrib import messages


def redirect_view(request):
   return redirect('sign_in_url')


@login_required()
def profile(request):
   img_profile = ProfileImage(instance=request.user.profile)
   update_user = UserUpdateForm(instance=request.user)
   print('test for git')
   if request.method == "POST":
      img_profile = ProfileImage(request.POST, request.FILES, instance=request.user.profile)
      update_user = UserUpdateForm(request.POST, instance=request.user)

      if img_profile.is_valid() and update_user.is_valid():
         img_profile.save()
         update_user.save()
         messages.success(request, f'Ваш аккаунт был успешно обнавлен!')
         return redirect('profile_url')

   return render(request, 'Users/profile.html', context={
      'img_profile': img_profile,
      'update_user': update_user,
   })