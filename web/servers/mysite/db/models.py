from django.db import models
from home import models as homeModels
from api import models as apiModels
# Create your models here.

# class Room(models.Model):
# 	number = models.TextField(max_length=200)
# 	hotel_id = models.ForeignKey(apiModels.Hotel, on_delete=models.CASCADE)
# 	roomtype_id = models.ForeignKey(homeModels.Roomtype, on_delete=models.CASCADE)

# 	def __str__(self):
# 		return self.id

# class Order(models.Model):
# 	user_id = models.DecimalField(max_digits=90, decimal_places=0, default=1)
# 	hotel_id = models.ForeignKey(apiModels.Hotel, on_delete=models.CASCADE)
# 	room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
# 	checkin_date = models.DateField(default='12-12-2020')
# 	checkout_date = models.DateField(default='13-12-2020')
# 	checkin_key = models.CharField(max_length=200, default='BK2001')

# 	def __str__(self):
# 		return self.id