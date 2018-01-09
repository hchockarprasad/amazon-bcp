from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login_view'),
]
