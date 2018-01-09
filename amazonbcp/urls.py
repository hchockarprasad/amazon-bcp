from django.urls import path, include

urlpatterns = [
    path('', include('dashboard.urls'), name='dashboard'),
    path('auth/', include('authentication.urls'), name='authentication'),
]
