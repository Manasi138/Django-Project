from django.db import models
from hotelapp.models import Hotel,Category
from userapp.models import Customer

class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    hotel=models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_category=models.ForeignKey(Category, on_delete=models.CASCADE)
    no_of_rooms=models.FloatField(default=0.0)
    no_of_people=models.IntegerField()
    check_in=models.DateTimeField()
    check_out=models.DateTimeField()
    total_price=models.FloatField(default=0.0)
    

# Create your models here.
