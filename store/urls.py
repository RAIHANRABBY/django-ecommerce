from django.urls import path
from . import views

urlpatterns = [
    path('', views.storeView, name='store'),
    path('cart/', views.cartView, name='cart'),
    path('checkout/', views.checkoutView, name='checkout'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('register/', views.registerView, name='register'),
    path('view/<str:pk>/', views.ViewProduct, name='view'),
    path('update_item/', views.updateItem,name='update_item')

]
