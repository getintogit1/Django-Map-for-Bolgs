# attractions/urls.py

from django.urls import path
from attractions import views


urlpatterns = [
    path("", views.attraction_index, name="attraction_index"),
    #path("<int:pk>/", views.attraction_detail, name="attraction_detail"),
    path('attractions/<slug:slug>/', views.attraction_detail, name='attraction_detail'),

]