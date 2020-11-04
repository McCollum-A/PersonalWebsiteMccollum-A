from django.urls import path
from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:Blog_id>/', views.blogentire, name='blogentire')
]
