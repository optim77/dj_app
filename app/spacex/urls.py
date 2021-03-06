from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('contact/', views.contact, name='contact'),
    path('category/<slug:slug>/', views.category, name='category'),
    path('item/<int:id>', views.item, name='item'),
    path('vendor/<int:id>', views.vendor, name='vendor'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('login/', views.login_page, name='login_page'),
    path('sign_up/', views.sign_up, name='sign_page'),
    path('logout', views.logout_user, name='logout'),
    path('add_new/', views.add_new, name='add_new'),
    path('edit/<str:id>/', views.update_item, name='update_item'),
    path('delete/<int:id>.', views.delete_item, name='delete_item'),
    path('add_to_basket/<int:id>', views.add_to_basket, name='add_to_basket')
]
