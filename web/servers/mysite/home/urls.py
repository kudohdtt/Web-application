from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('', views.index,name ='index'),
   # path('login/', views.login,name ='login'),
   path('rooms/<int:hotel_id>/', views.rooms,name ='rooms'),
   path('roomdetail/<int:roomtype_id>/', views.roomdetail,name ='room-detail'),
   path('register/', views.register, name="register"),
   path('login/',auth_views.LoginView.as_view(template_name="login.html"), name="login"),
   path('logout/',auth_views.LogoutView.as_view(next_page='/bookingroom/login/'),name='logout'),
   path('hotels', views.hotels,name ='hotels'),
   path('blog', views.blog,name ='blog'),
   path('order/', views.order,name ='order'),
   path('orderdetail/', views.orderdetail,name ='orderdetail'),
   path('sendEmailConfirm/', views.sendEmailConfirm,name ='sendEmailConfirm'),
   path('order/c/', views.createOrder,name ='createOrder'),
   path('order/d/', views.deleteOrder,name ='deleteOrder'),
]
