from django.urls import path
from . import views

urlpatterns = [
    path("c/",views.displaycustomer,name="c"),
    path("c_show/",views.showCustomers,name="c_show"),
    path("c_save/",views.saveCustomers,name="c_save"),
    path("c_show/edit/<int:emailId>",views.getCustomerById,name="edit"),
    path("c_show/delete/<int:emailId>",views.deleteCustomerById,name="delete"),
]