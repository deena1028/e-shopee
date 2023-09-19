from django.db import models


# Create your models here.
class category(models.Model):
    catId=models.IntegerField(null=True)
    catName=models.TextField(null=True)
class product(models.Model):
    pId=models.IntegerField(null=True)
    pName=models.TextField(max_length=200)
    pdec=models.TextField(max_length=500)   
    pPrice=models.FloatField(max_length=200)
    pQty=models.IntegerField(null=True) 
    catId=models.IntegerField(null=True) 
    cover = models.ImageField(upload_to = 'images/')
    
    
class cart(models.Model):
    cartId=models.IntegerField(null=True)
    userId=models.TextField(max_length=100,null=True)
    cartQty=models.IntegerField(null=True)
    pId=models.ForeignKey(product, null=True, on_delete=models.CASCADE)
    ppid=models.IntegerField(null=True)
    pprice=models.IntegerField(null=True)
    pname=models.TextField(max_length=200,null=True)
    pcover=models.TextField(max_length=200,null=True)
    tqty=models.IntegerField(null=True)
    
    

class login1(models.Model):  
    username=models.TextField(max_length=200)     
    paswod=models.TextField(max_length=200)