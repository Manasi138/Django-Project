from django.urls import path
from . import views

urlpatterns = [
    path("d/",views.displayhotel,name="d"),
    path("show/",views.showHotels,name="show"),
    path("update/",views.saveHotels,name="update"),
    path("show/edit/<int:hotelId>",views.getHotelById,name="edit"),
    path("show/delete/<int:hotelId>",views.deleteHotelById,name="delete"),
    path("show/detail/<int:hotelId>",views.addCategory,name="detail"),
    path("show/clist/<int:hotelId>",views.allCategory,name="clist"),
    path("show/deletecat/<int:Id>",views.deleteCatById,name="deletecat"),
    path("show/editcat/<int:Id>",views.getCatById,name="deletecat"),
]
