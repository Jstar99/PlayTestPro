from django.urls import path
from . import views


urlpatterns = [
    path('', views.Homepage),
    path('home/', views.Homepage),
    path('projects/', views.ProjectsPage),  
    path('ProjectEnnead/', views.ProjectEnnead),  
    path('Points/', views.PointsPage),  
]


