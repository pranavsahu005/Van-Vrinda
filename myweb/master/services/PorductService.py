from django.shortcuts import render,HttpResponse,redirect
from django.core.files.storage import FileSystemStorage
from master.Entity.product import Product
from master.Repository.Productrepo import productRepo

class ProductService:
    def __init__(self):
        self.repo=productRepo()
    def addProduct(self,data):
        product=Product()
        product.pname=data['pname']
        product.description=data['description']
        product.price=data['price']
        image=data.FILES.get('image')
        if image:
            fs=FileSystemStorage(image)
            product.image=fs.save(image.name,image)
        else:
            product.image="none"
        product.cid=data['category']
        product.plant_size=data['plant_size']
        product.plant_weight=data['plant_weight']
        product.soil_type=data['soil_type']

        return self.repo.addProduct(product)
        
            
        