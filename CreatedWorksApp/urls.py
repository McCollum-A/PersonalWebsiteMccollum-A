from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:Works_id>/', views.projectabstract, name='projectabstract')
]
