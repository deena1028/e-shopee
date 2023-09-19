from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import product,category,cart,login1
import random
import json

# Create your views here.
def index(request):
     cat=category.objects.all().values()
     pdct=product.objects.all().values()
     pdata={'category':cat,'product':pdct}
     return render(request,'index.html',pdata)
def login(request):

     return render(request,'login.html')
def login_user(request):
      if(request.method=="POST"):
             userid=request.POST.get('userid')
             paswod=request.POST.get('paswod')
             check_user = login1.objects.filter(username=userid,paswod=paswod)
             if check_user:
                   request.session['user'] = userid
                   request.session['logined'] = 1
                   return redirect('/home')
def updateCartitem(request):
     is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

     if is_ajax:
        
        if request.method == 'POST':
            data = json.load(request)
            todo = data.get('pid')
            if 'user' not in request.session:
                 my_list = [1, 2, 3, 4, 5, 6,7,8,9,0]
                 userid=random.choice(my_list)
            
            else:
                 userid=request.session['user']
             
            check_cart = cart.objects.filter(userId=userid,ppid=todo) 
            cartid=5000
            if check_cart:
               dts=cart.objects.get(userId=userid,ppid=todo)
               dts.cartQty=int(dts.cartQty)+1
               pqty=int(dts.cartQty)+1
               tqty=(pqty*dts.pprice)
               dts.tqty=(pqty*dts.pprice)
               dts.save()
            else:
               pqty=1
               news_obj = product.objects.get(pId=todo)
               tqty=pqty*int(news_obj.pPrice)
               query=cart(cartId=cartid,userId=userid,cartQty=pqty,pId=news_obj,ppid=todo,pprice=news_obj.pPrice,pname=news_obj.pName,pcover=news_obj.cover,tqty=tqty)
               query.save()
     
           
            return JsonResponse({'qty':pqty,'tqty':tqty})
def viewcart(request):
     cartdata=cart.objects.all().values()
     cartdt={'cart':cartdata}
     
     return render(request,'cart.html',cartdt)

def delete_cart(request):
     is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

     if is_ajax:
        
        if request.method == 'POST':
            data = json.load(request)
            todo = data.get('pid')
            if 'user' not in request.session:
                 my_list = [1, 2, 3, 4, 5, 6,7,8,9,0]
                 userid=random.choice(my_list)
            
            else:
                 userid=request.session['user']
             
            check_cart = cart.objects.filter(userId=userid,ppid=todo) 
            cartid=5000
            if check_cart:
               dts=cart.objects.get(userId=userid,ppid=todo)
               ccqty=dts.cartQty
               pqty=int(ccqty)-1
               tqty=(pqty*dts.pprice)
               dts.tqty=(pqty*dts.pprice)
               if pqty>0:
                    dts.cartQty=pqty
                    dts.save()
               else:
                    dts.delete()
            return JsonResponse({'qty':pqty,'tqty':tqty})
def checkout(request):
     return render(request,'checkout.html')

def logout(request):
     del request.session['user']
     del request.session['logined']
     return redirect('index')    
def shop(request):
     cat=category.objects.all().values()
     pdct=product.objects.all().values()
     pdata={'category':cat,'product':pdct}
     return render(request,'shop.html',pdata)
def search(request):
     if request.method == 'POST':
          search_data= request.POST.get('search')  
          if search_data:
            results = product.objects.filter(pName__contains=search_data)
            if results:
               catid=[]
               for i in results:
                    catid.append(i.catId)
                              
               cat=category.objects.filter(catId__in=catid)
               
               pdata={'category':cat,'product':results,'datacount':1}
            else:
               pdata={'category':cat,'product':results,'datacount':0}
                 
            return render(request,'shop.html',pdata)
           
                

def search_category(request,id):
      results = product.objects.filter(catId=id) 
      cat=category.objects.filter(catId=id)     
      pdata={'category':cat,'product':results}
      return render(request,'shop.html',pdata) 
            
                          

           
            
            