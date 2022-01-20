from .views import RecordView, RecordTrialView, LogView
from django.urls import path
from.import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('record/', RecordTrialView.as_view(), name='record'),
    path('signup/', views.signup, name="signup"),
    path('home/record/', RecordView.as_view(), name="record_home"),
    path('log/', LogView.as_view(), name="log"),
    path('delete/', LogView.as_view(), name="delete"),
]
