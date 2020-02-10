from django.urls import path, include
from .views import dashboard, create_user, dash, sign_in


app_name = 'dashboard'
urlpatterns = [
    path('dashboard', dashboard, name='dashboard'),
    
    
]