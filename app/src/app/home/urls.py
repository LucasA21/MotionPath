from django.urls import path
from .views.home_view import HomeView
from app.home.views.dashboard_view import DashboardView
from .views.construction_view import ConstructionView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('construction/', ConstructionView.as_view(), name='construction'),
]
