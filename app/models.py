from django.db import models

# Create your models here.

# User Side Data

class User(models.Model):
    Username = models.CharField(max_length=100,default="xyz@12")
    Ufname = models.CharField(max_length=255,default="Seller Name")
    Ulname = models.CharField(max_length=255,default="Shop Name")
    Uemail = models.EmailField(unique=True)
    Umobile = models.BigIntegerField(default="123")
    Uaddress1 = models.CharField(max_length=255,default="Address1",null=True)
    Uaddress2 = models.CharField(max_length=255,default="Address2",null=True)
    UCity = models.CharField(max_length=255,default="City",null=True)
    UState = models.CharField(max_length=255,default="State",null=True)
    UPincode = models.IntegerField(default="000000")
    Upassword = models.CharField(max_length=255,default="password")
    UOTP = models.IntegerField(default="123456")

    def __str__(self):
        return self.Ufname

# Seller Site Data

class seller(models.Model):
    username = models.CharField(max_length=100,default="xyz@12")
    Sname = models.CharField(max_length=255,default="Seller Name")
    shop_name = models.CharField(max_length=255,default="Shop Name")
    email = models.EmailField(unique=True)
    mobile = models.BigIntegerField(default="123")
    address1 = models.CharField(max_length=255,default="Address 1")
    address2 = models.CharField(max_length=255,default="Address 2")
    City = models.CharField(max_length=200,default="City")
    state = models.CharField(max_length=200,default="state")
    Pincode = models.IntegerField(default="000000")
    password = models.CharField(max_length=255,default="password")
    OTP = models.IntegerField(default="123456")

    def __str__(self):
        return self.Sname

# Category

class Category(models.Model):
    pcategory = models.CharField(max_length=255,default="Product Category")

    def __str__(self):
        return self.pcategory

# Product Data

class Product(models.Model):
    Seller_ID = models.ForeignKey(seller, on_delete=models.CASCADE)
    Product_Name = models.CharField(max_length=255,default="Product Name")
    Product_Title = models.CharField(max_length=255,default="Product Name")
    Product_Image = models.ImageField(upload_to="productimages/",default="abc.jpg")
    Product_Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Product_Price = models.FloatField(default=0.0)
    Product_MRP = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.Product_Name

# Rating Data

class Rating(models.Model):
    getuser = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1)
    Review = models.CharField(max_length=255,default="Very Nice")
    Review_Date = models.DateField(auto_now_add=True)
    getprod = models.ForeignKey(Product, on_delete=models.CASCADE,default=True)

# Cart Data

class Cart(models.Model):
    getprod = models.ForeignKey(Product, on_delete=models.CASCADE,default=True)
    User_Id = models.ForeignKey(User, on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=1)
    Total = models.FloatField(default=250.0)
   
# Order Data

class Order(models.Model):
    Id = models.IntegerField(primary_key=True,default=123456)
    Order_Date = models.DateField(auto_now_add=True)
    User_Id = models.ForeignKey(User, on_delete=models.CASCADE)
    Seller_Id = models.ForeignKey(seller, on_delete=models.CASCADE)
    # cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.Id
