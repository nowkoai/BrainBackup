from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('signup/', views.signup, name="signup"),
    path('add/', views.AddView.as_view(), name='add'),
    path('search/', views.SearchView.as_view(), name='search')
]
