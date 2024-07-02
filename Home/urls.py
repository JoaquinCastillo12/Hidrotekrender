from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('category/<str:foo>/', views.category, name='category'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('adjust_cart/<int:item_id>/', views.adjust_cart, name='adjust_cart'),
    path('procesar_formulario/', views.procesar_formulario, name='procesar_formulario'),
]
