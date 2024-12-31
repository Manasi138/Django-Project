from django.shortcuts import render
from hotelapp.models import Hotel,Category
from userapp.models import Customer

def addbooking(request,id):
    if request.method!='POST':
     cat_data=Category.objects.get(id=id)
     return render(request, 'AddBooking.html')
# Create your views here.
