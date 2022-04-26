from django.urls import path
from .views import RegistrationView, UserLoginView, UserLogoutView, ProfileUpdateView


urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('<int:pk>/profile/', ProfileUpdateView.as_view(), name='profile'),
]
