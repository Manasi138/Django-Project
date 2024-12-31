from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def displayhotel(request):
    if request.method == 'POST':
        HotelName=request.POST['hotelName']
        Location=request.POST['location']
        HotelType=request.POST['hoteltype']
        Address=request.POST['address']
        Rating=request.POST['rating']
        Contact_No =request.POST['contact']
        images=request.FILES['hotel_image']
        new_hotel=Hotel(hotelName=HotelName,location=Location,hoteltype=HotelType,address=Address,rating=Rating,contact=Contact_No,hotel_image=images) # type: ignore
        Hotel.save(new_hotel)
        return HttpResponse("<h1> Success .....</h1>")
    else:
        return render(request, 'Addhotels.html')

def showHotels(request):
    data=Hotel.objects.all()
    return render(request, 'HotelList.html',{'hotels':data})

def saveHotels(request):
    if request.method == 'POST':
        HotelName=request.POST['hotelName']
        Location=request.POST['location']
        HotelType=request.POST['hoteltype']
        Address=request.POST['address']
        Rating=request.POST['rating']
        Contact_No =request.POST['contact']
        images=request.FILES['hotel_image']
        hId=request.POST['hotelId']
        data=Hotel.objects.filter(hotelId=hId)
        data.update(hotelName=HotelName,location=Location,hoteltype=HotelType,address=Address,rating=Rating,contact=Contact_No,hotel_image=images) # type: ignore
        return HttpResponse("<h1> Success .....</h1>")
    else:
        return render(request, 'UpdateHotel.html')
    
def getHotelById(request,hotelId):
    data=Hotel.objects.get(hotelId=hotelId)
    return render (request,"UpdateHotel.html",{"hotel": data})

def deleteHotelById(request,hotelId):
    data=Hotel.objects.get(hotelId=hotelId)
    data.delete()
    return HttpResponse("<h1>Success ....")
    
    
def addCategory(request,hotelId):
    if request.method != 'POST':
        data=Hotel.objects.get(hotelId=hotelId)
        return render(request,"AddCategory.html",{"hotel_1":data})
    else:
        data=Hotel.objects.get(hotelId=hotelId)
        roomno=request.POST['room_No']
        roomtype=request.POST['roomType']
        roomprice=request.POST['price_per_room']
        available=request.POST['available_room']
        data_c=Category(hotel=data,room_No=roomno,roomType=roomtype,price_per_room=roomprice,available_room=available)
        data_c.save()
        return HttpResponse("<h1>Success ....")
    
def allCategory(request,hotelId):
    h_data=Hotel.objects.get(hotelId=hotelId)
    c_data=Category.objects.filter(hotel=h_data)
    return render(request,"CategoryList.html",{"cat_data":c_data})

def getCatById(request,Id):
    c_data=Category.objects.get(Id=Id)
    return render (request,"CategoryList.html",{"cat_data": c_data})

def deleteCatById(request,Id):
    c_data=Category.objects.get(Id=Id)
    if request.method == 'Post':
        c_data.delete()
        return HttpResponse("<h1>Success ....")    
# Create your views here.
