from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('client/<int:pk>', views.customer_client, name='client'),
    path('delete_client/<int:pk>', views.delete_client, name='delete_client'),
    path('add_client/', views.add_client, name='add_client'),    
    path('update_client/<int:pk>', views.update_client, name='update_client'),    
]
