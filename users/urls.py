
from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import LMSLoginView, SignUpView

app_name = 'users'

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', LMSLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
