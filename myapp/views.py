from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index-4.html')

def pro1(request):
    return render(request,'product.html')