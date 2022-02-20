import re
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import speech_recognition as sr
from .models import Blog, InputText
from django.contrib.auth import login
from .form import UserCreationForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user_instance = form.save()
            login(request, user_instance)
            return redirect("app:index")
    else:
        form = UserCreationForm()

    context = {
        "form": form
    }
    return render(request, 'app/signup.html', context)


class IndexView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        blog_data = Blog.objects.all()
        return render(request, 'app/index.html', {
            'blog_data': blog_data,
        })
class AddView(LoginRequiredMixin,View):
    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')

        blog = Blog()
        blog.title = title
        blog.save()

        data = {
            'title': title,
        }
        return JsonResponse(data)

class SearchView(LoginRequiredMixin,View):
    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        blog_data = Blog.objects.all()
        title_list = []

        if title:
            blog_data = blog_data.filter(title__icontains=title)

        for blog in blog_data:
            title_list.append(blog.title)

        data = {
            'title_list': title_list,
        }
        return JsonResponse(data)
