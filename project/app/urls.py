from .views import RecordView, RecordTrialView, LogView,IndexView
from django.urls import path
from .import views
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('home/', views.home, name='home'),
    path('record/', RecordTrialView.as_view(), name='record'),
    path('signup/', views.signup, name="signup"),
    path('home/record/', RecordView.as_view(), name="record_home"),
    path('log/', LogView.as_view(), name="log"),
    path('delete/', LogView.as_view(), name="delete"),
    path('add/', views.AddView.as_view(), name='add'),

]
