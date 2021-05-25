from django.contrib import admin
from home.models import Roomtype, Room, Order, Blog, Rating, Comment

admin.site.register(Roomtype)
admin.site.register(Room)
admin.site.register(Order)

admin.site.register(Blog)
admin.site.register(Rating)
admin.site.register(Comment)
# Register your models here.
