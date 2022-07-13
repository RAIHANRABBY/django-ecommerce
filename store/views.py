from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Product,Order,OrderItem
from .forms import UserReg
from django.contrib.auth import login,logout,authenticate
import json
# Create your views here.
def cartView(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created =Order.objects.get_or_create(customer=customer, complete = False)
        items=order.orderitem_set.all()
    else:
        items=[]
        order={'get_total_price':0,'get_total_item':0}

    
    content={'items':items,'order':order}
    return render(request,'store/cart.html',content)

def storeView(request):
    product=Product.objects.all()

    content={'products':product}
    return render(request,'store/store.html',content)

def checkoutView(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created =Order.objects.get_or_create(customer=customer, complete = False)
        items=order.orderitem_set.all()
    else:
        items=[]
        order={'get_total_price':0,'get_total_item':0}

    
    content={'items':items,'order':order}
    return render(request,'store/checkout.html',content)


def loginView(request):
    logstate=True
    if request.user.is_authenticated:
        return redirect('store')

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username)
        except :
            messages.error(request,'User does not exist.')

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('store')
        else:
            messages.error(request,'Wrong Username/password')
    content={'login':logstate}

    return render(request,'store/register_login.html',content)


def logoutView(request):
   
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')


def registerView(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    form=UserReg()
    if request.method == 'POST':
        form=UserReg(request.POST)
        if form.is_valid:
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            messages.success(request,'Account Successfully Created!')
            return redirect('store')

        else:
            form=UserReg()
            messages.error(request,'Something went wrong!')
    
    
    content={'form':form}
    return render(request,'store/register_login.html',content)


def ViewProduct(request,pk):
    product =Product.objects.get(id=pk)
    content={'product':product}
    return render(request,'store/productviewpage.html',content)

def updateItem(request):
    data = json.loads(request.data)
    productId=data['productId']
    action = data['action']
    print(productId)
    print(action)
    return JsonResponse('Item was added', safe=False)