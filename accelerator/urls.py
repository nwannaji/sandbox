from django.urls import path
from .api_views import (
    AgriTechSensorDataListCreateView, AgriTechSensorDataDetailView,
    MedTechSensorDataListCreateView, MedTechSensorDataDetailView,
    FinTechSensorDataListCreateView, FinTechSensorDataDetailView,
    OtherSensorDataListCreateView, OtherSensorDataDetailView
)
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_sensor_data, name='add_sensor_data'),
    path('view/', views.view_sensor_data, name='view_sensor_data'),
    path('analytics/', views.analytics_dashboard, name='data_visualization'),
    path('login/', auth_views.LoginView.as_view(template_name='accelerator/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # AgriTech API Endpoints
    path('api/agritech/', AgriTechSensorDataListCreateView.as_view(), name='agritech-list'),
    path('api/agritech/<int:pk>/', AgriTechSensorDataDetailView.as_view(), name='agritech-detail'),

    # MedTech API Endpoints
    path('api/medtech/', MedTechSensorDataListCreateView.as_view(), name='medtech-list'),
    path('api/medtech/<int:pk>/', MedTechSensorDataDetailView.as_view(), name='medtech-detail'),

    # FinTech API Endpoints
    path('api/fintech/', FinTechSensorDataListCreateView.as_view(), name='fintech-list'),
    path('api/fintech/<int:pk>/', FinTechSensorDataDetailView.as_view(), name='fintech-detail'),

    # Other Sensor API Endpoints
    path('api/other/', OtherSensorDataListCreateView.as_view(), name='other-list'),
    path('api/other/<int:pk>/', OtherSensorDataDetailView.as_view(), name='other-detail'),
]