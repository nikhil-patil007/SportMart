from django.shortcuts import render,redirect
from .models import *
from app.models import *

def index(request):
    if 'aid' in request.session:
        usr = User.objects.all()
        slr = seller.objects.all()
        pro = Product.objects.all()
        odr = Orders.objects.all()
        cat = Category.objects.all()
        rat = Rating.objects.all()
        a = usr.count()
        b = slr.count()
        c = pro.count()
        d = odr.count()
        e = cat.count()
        f = rat.count()
        return render(request, "admin_site/index.html",{'a':a,'b':b,'c':c,'d':d,'e':e,'f':f})
    else:
        return redirect("login")

def A_User(request):
    if 'aid' in request.session:
        usr = User.objects.all()
        return render(request, "admin_site/All-Users.html",{'usr':usr})
    else:
        return redirect("login")

def A_seller(request):
    if 'aid' in request.session:
        slr = seller.objects.all()
        return render(request, "admin_site/All-Sellers.html",{'slr':slr})
    else:
        return redirect("login")

def A_Products(request):
    if 'aid' in request.session:
        pro = Product.objects.all()
        return render(request, "admin_site/All-Products.html",{'pro':pro})
    else:
        return redirect("login")

def A_Category(request):
    if 'aid' in request.session:
        cat = Category.objects.all()
        return render(request, "admin_site/All-Category.html",{'cat':cat})
    else:
        return redirect("login")

def A_Order(request):
    if 'aid' in request.session:
        odr = Orders.objects.all()
        return render(request, "admin_site/Order.html",{'odr':odr})
    else:
        return redirect("login")

def A_Rat(request):
    if 'aid' in request.session:
        rat = Rating.objects.all()
        return render(request, "admin_site/Rating.html",{'rat':rat})
    else:
        return redirect("login")

def del_User(request,pk):
    try:
        usr = User.objects.get(id=pk)
        usr.delete()
        return redirect("AUsers")
    except:
        return redirect("AUsers")

def del_Seller(request,pk):
    try:
        slr = seller.objects.get(id=pk)
        slr.delete()
        return redirect("Aseller")
    except:
        return redirect("Aseller")
    
def del_Product(request,pk):
    try:
        pro = Product.objects.get(id=pk)
        pro.delete()
        return redirect("Aproduct")
    except:
        return redirect("Aproduct")

def A_A_Category(request):
    if 'aid' in request.session:
        ca = request.POST['ca']

        cat = Category.objects.create(
            pcategory=ca
        )
        return redirect("Acat")
    else:
        return redirect("login")

def del_Category(request,pk):
    try:
        cat = Category.objects.get(id=pk)
        cat.delete()
        return redirect("Acat")
    except:
        return redirect("Acat")

def del_Rating(request,pk):
    try:
        rat = Rating.objects.get(id=pk)
        rat.delete()
        return redirect("Arat")
    except:
        return redirect("Arat")

def login(request):
    if 'aid' in request.session:
        return redirect("Aindex")
    else:
        return render(request, "admin_site/Login.html")

def A_login(request):
    try:
        ur = request.POST['email']
        pwd = request.POST['pswd']

        user = Admin.objects.filter(Username=ur)
        if len(user) > 0:
            if user[0].Upassword == pwd:
                request.session['aid']= user[0].id
                return redirect("Aindex")
            else:
                msg = "Password is Incorrect..!"
                return render(request, "admin_site/Login.html",{'err':msg})
        else:
            msg = "User Doesn't Found"
            return render(request, "admin_site/Login.html",{'err':msg})
    except:
        return redirect("login")

def A_logout(request):
    try:
        del request.session['aid']
        return redirect("login")
    except:
        return redirect("login")
