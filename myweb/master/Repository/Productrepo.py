from django.db import connection
from django.shortcuts import render,HttpResponse,redirect
from django.core.files.storage import FileSystemStorage
ob=connection.cursor()
class productRepo:
    def addProduct(self,product):
        data=[product.pname,product.description,product.price,product.image,product.cid,product.plant_size,product.plant_weight,product.soil_type]    
        ob.execute("insert into product(pname,description,price,image,cid,plant_size,plant_weight,soil_type) values (%s,%s,%s,%s,%s,%s,%s,%s)",data)
        return product.pname," is added!"