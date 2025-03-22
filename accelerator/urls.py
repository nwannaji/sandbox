from django.urls import path

from .api_views import SensorDataDetailView, SensorDataListCreateView
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_sensor_data, name='add_sensor_data'),
    path('view/', views.view_sensor_data, name='view_sensor_data'),
    path('login/', auth_views.LoginView.as_view(template_name='accelerator/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #API views URL
    path('api/sensor-data/', SensorDataListCreateView.as_view(), name='sensor-data-list'),
    path('api/sensor-data/<int:pk>/', SensorDataDetailView.as_view(), name='sensor-data-detail'),
]