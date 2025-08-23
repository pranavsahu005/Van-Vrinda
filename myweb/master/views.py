from django.shortcuts import render,HttpResponse
from master.services.PorductService import ProductService
service=ProductService()
def addProduct(request):
    if(request.method=='POST'):
        
        return HttpResponse(service.addProduct(request.POST))
    else:
        return render(request,"admin/addproduct.html")


