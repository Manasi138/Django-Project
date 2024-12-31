from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def displaycustomer(request):
    if request.method == 'POST':
        CustomerName=request.POST['C_name']
        CustomerPassword=request.POST['C_password']
        Aadhar_No=request.POST['aadhar_no']
        Address=request.POST['address']
        Contact_No =request.POST['contact']  
        new_customer=Customer(C_name=CustomerName,C_password=CustomerPassword,aadhar_no=Aadhar_No,address=Address,contact=Contact_No) # type: ignore
        Customer.save(new_customer)
        return HttpResponse("<h1> Success .....</h1>")
    else:
        return render(request, 'AddCustomer.html')
    
def showCustomers(request):
    data=Customer.objects.all()
    return render(request, 'CustomerList.html',{'customers':data})

def saveCustomers(request):
    if request.method == 'POST':
        EmailId=request.POST['emailId']
        CustomerName=request.POST['C_name']
        CustomerPassword=request.POST['C_password']
        Address=request.POST['address']
        Aadhar_No=request.POST['aadhar_no']
        Contact_No =request.POST['contact']
        data=Customer.objects.filter(emailId=EmailId)
        data.update(C_name=CustomerName,C_password=CustomerPassword,aadhar_no=Aadhar_No,address=Address,contact=Contact_No) # type: ignore
        return HttpResponse("<h1> Success .....</h1>")
    else:
        return render(request, 'UpdateCustomer.html')
    
def getCustomerById(request,emailId):
    data=Customer.objects.get(emailId=emailId)
    return render (request,"UpdateCustomer.html",{"customer": data})

def deleteCustomerById(request,emailId):
    data=Customer.objects.get(emailId=emailId)
    data.delete()
    return HttpResponse("<h1>Success ....")
# Create your views here.
