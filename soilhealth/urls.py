from django.urls import path
from . import views

app_name = 'soilhealth'

urlpatterns = [
    path('', views.home, name='home'),
    path('recommendations/', views.recommendations, name='recommendations'),
    path('soil-sample/', views.soil_sample, name='soil_sample'),
    path('climate-insights/', views.climate_insights, name='climate_insights'),
]
