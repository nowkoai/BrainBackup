from .views import RecordView
from .views import RecordTrialView
from django.urls import path
from.import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('record/', RecordTrialView.as_view(), name='record'),
    path("signup/", views.signup, name="signup"),
    path("home/record/", RecordView.as_view(), name="record_home"),
]