import re
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import speech_recognition as sr
from .models import Neuron, Synapse
from django.contrib.auth import login
from .form import UserCreationForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Neuron


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
        neuron_data = Neuron.objects.all()
        return render(request, 'app/index.html', {
            'neuron_data': neuron_data,
        })
class AddView(LoginRequiredMixin,View):
    def post(self, request, *args, **kwargs):
        text = request.POST.get('text')

        neuron = Neuron()
        neuron.text = text
        neuron.save()

        data = {
            'text': text,
        }
        return JsonResponse(data)

class SearchView(LoginRequiredMixin,View):
    def post(self, request, *args, **kwargs):
        text = request.POST.get('text')
        neuron_data = Neuron.objects.all()
        text_list = []

        if text:
            neuron_data = neuron_data.filter(text__icontains=text)

        for neuron in neuron_data:
            text_list.append(neuron.text)

        data = {
            'text_list': text_list,
        }
        return JsonResponse(data)
