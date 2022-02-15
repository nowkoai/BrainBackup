from django.urls import path
from app import views
from django.contrib.auth import views as auth_views

app_name = 'app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name="signup"),
    path('add/', views.AddView.as_view(), name='add'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
 ]
