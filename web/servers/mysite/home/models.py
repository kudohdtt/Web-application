from django.db import models
from api import models as apiModels

# Create your models here.
class Roomtype(models.Model):
	name = models.CharField(max_length=200)
	script = models.TextField()
	hotel_id = models.ForeignKey(apiModels.Hotel, on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=100, decimal_places=2, default=100)
	image = models.CharField(max_length=200, default="/static/templates/rooms/images/photos/9.jpg")
	bed = models.CharField(max_length=200, default="1 Large bed")
	acreage = models.DecimalField(max_digits=100, decimal_places=2, default=0)
	service_bonus = models.CharField(max_length=200, default=None)

	def __str__(self):
		return self.name 


class Room(models.Model):
	number = models.TextField()
	hotel = models.ForeignKey(apiModels.Hotel, on_delete=models.CASCADE)
	roomtype = models.ForeignKey(Roomtype, on_delete=models.CASCADE)

	def __str__(self):
		return self.number

class Order(models.Model):
	user_id = models.DecimalField(max_digits=90, decimal_places=0, default=1)
	hotel = models.ForeignKey(apiModels.Hotel, on_delete=models.CASCADE)
	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	checkin_date = models.DateField(default='2020-12-12')
	checkout_date = models.DateField(default='2020-12-13')
	checkin_key = models.CharField(max_length=200, default='BK2001')

	def __str__(self):
		return self.checkin_key


class Blog(models.Model):
	hotel = models.ForeignKey(apiModels.Hotel, on_delete=models.CASCADE)

class Rating(models.Model):
	hotel = models.ForeignKey(apiModels.Hotel, on_delete=models.CASCADE)
	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	user_id = models.DecimalField(max_digits=90, decimal_places=0, default=1)

class Comment(models.Model):
	hotel = models.ForeignKey(apiModels.Hotel, on_delete=models.CASCADE)
	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	user_id = models.DecimalField(max_digits=90, decimal_places=0, default=1)