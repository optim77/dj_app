from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('contact/', views.contact, name='contact'),
    path('category/<slug:slug>/', views.category, name='category'),
    path('login/', views.login_page, name='login_page'),
    path('logout', views.logout_user, name='logout'),
    path('add_new/', views.add_new, name='add_new')
]