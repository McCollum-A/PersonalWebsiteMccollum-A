from django.urls import path
from . import views

urlpatterns = [
    path('', views.allportfolio, name='allportfolio'),
    path('<int:Portfolio_id>/', views.portfoliodetail, name='portfoliodetail')
]
