from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Comment
from .forms import CommentForm
from django.contrib import messages
from django.views.generic import (
   View,
   ListView, 
   DetailView, 
   CreateView,
   UpdateView,
   DeleteView,
)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



def news(request):
   posts = Post.objects.all()
   return render(request, 'News/news.html', context={
      'posts':posts,
   })


class ShowNewsView(ListView):
   model = Post
   template_name = 'News/news.html'
   context_object_name = 'posts'
   ordering = ['-date']
   paginate_by = 5

   # def get_context_data(self, **kwargs):
   #    ctx = super(ShowNewsView, self).get_context_data(**kwargs)
   #    ctx['title'] = 'Главная страница блога'
   #    return ctx 

class NewsDetailView(View):
   def get(self, request, pk):
      post = get_object_or_404(Post, pk=pk)
      comments = Comment.objects.filter(post=post, approved=True).order_by('-date')
      comment_form = CommentForm()
      return render(request, 'News/news_detail.html', context={
         'post': post,
         'comments': comments,
         'comment_form': comment_form,
      })
   def post(self, request, pk):
      post = get_object_or_404(Post, pk=pk)
      bound_form = CommentForm(request.POST)
      if bound_form.is_valid():
         text = request.POST.get('text')
         full_name = request.POST.get('full_name')
         comment = Comment.objects.create(post=post, full_name=full_name, text=text)
         comment.save()
         messages.success(request, f'Ваш комментарий в рассмотрений')
         return redirect(post)
      return redirect(post)


class CreateNewsView(LoginRequiredMixin, CreateView):
   model = Post
   fields = ('title', 'text', 'img')

   def form_valid(self, form):
      form.instance.author = self.request.user
      return super().form_valid(form)


class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
   model = Post
   template_name = 'News/post_update.html'
   fields = ('title', 'text', 'img')

   def form_valid(self, form):
      form.instance.author = self.request.user
      return super().form_valid(form)

   def test_func(self):
      post = self.get_object()
      if self.request.user == post.author:
         return True
      return False


class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
   model = Post
   success_url = '/'

   def form_valid(self, form):
      form.instance.author = self.request.user
      return super().form_valid(form)

   def test_func(self):
      post = self.get_object()
      if self.request.user == post.author:
         return True
      return False