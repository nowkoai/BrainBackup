from .views import MyView
from django.urls import path
from.import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('record/', MyView.as_view(), name='record'),
    path("signup/", views.signup, name="signup"),
]
