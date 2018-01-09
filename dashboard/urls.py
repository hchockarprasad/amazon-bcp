from django.urls import path

from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(template_name='dashboard.html'), name='dashboard_view'),
]
