from django.urls import path
from User import views as user_views

urlpatterns = [
    
    path('register/', user_views.UserRegisterView.as_view(), name='user_register'),
    path('login/', user_views.LoginView.as_view(), name='login'),

]