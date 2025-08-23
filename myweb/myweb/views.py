from django.shortcuts import render,HttpResponse,redirect

def front(request):
    return render(request,'front.html')

def homepage(request):
    return render(request,'homepage.html')

def signin(request):
    return render(request,'signin.html')

def signup(request):
    return render(request,'signup.html')
def addProduct(request):
    return render(request,'addproduct.html')