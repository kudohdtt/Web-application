from django.urls import path
  
from api import views

urlpatterns = [
    path('hotels', views.ListCreateHotelView.as_view()),
    path('hotels/<int:pk>', views.UpdateDeleteHotelView.as_view()),
    path('search', views.FindbyName, name='search'),
]