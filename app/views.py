from django.http import JsonResponse
from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from random import randint

# Create your views here.


# USER SIDE FUNCTIONS
def qty(request):
    print("HERE I AM")
    qt = request.POST['fname']

    us= Cart.objects.create(Quantity=qt)

    alldata = list(Cart.objects.values())

    return JsonResponse({'res':alldata})

# Page Functions.

# User Login page
def U_Loginpage(request):
    if 'uid' in request.session:
        return redirect("index")
    else:
        return render(request, "app/user-login.html")

# User Register page
def U_Registerpage(request):
    if 'uid' in request.session:
        return redirect("index")
    else:
        return render(request, "app/user-Register.html")

# User index page
def U_Indexpage(request):
    pr = Product.objects.all()
    return render(request, "app/user-index.html",{'pro' : pr})

# User cart page
def U_Cart(request):
    if 'uid' in request.session:
        shi = Cart.objects.filter(User_Id=request.session['uid'])
        return render(request, "app/Cart.html",{'shi':shi})
    else:
        return redirect('Userlogin')

# User forgot password page
def U_Forgot_Page(request):
    return render(request, "app/user-Forgot-Password.html")

# User Enter otp
def U_OTP_page(request):
    return render(request, "app/user-Enter OTP.html")

# User recover page
def U_recov_Page(request):
    return render(request, "app/user-Recover-Password.html")

# User profile
def U_Profile(request):
    if 'uid' in request.session:
        getuser = User.objects.get(id=request.session['uid'])
        return render(request, "app/user-Profile.html",{'user': getuser})
    else:
        return redirect("index")

# User change password
def U_Changepaspage(request):
    return render(request, "app/user-changepass.html")

# User order page
def U_Orderpage(request):
    return render(request, "app/user-order.html")

# User order track
def U_Trackpage(request):
    return render(request, "app/order-tracking.html")

# User complete order
def Completpage(request):
    return render(request, "app/Check-out.html")

# User Show Page
def U_showpage(request,pk):
    ProductData = Product.objects.get(id=pk)
    rv = Rating.objects.filter(getprod=ProductData)
    count=rv.count()
    return render(request, "app/User-View-Product.html",{'data':ProductData,'rev':rv,"count":count})

# Method Functions.

# def orders(request):
#     if 'uid' in request.session:
#         getuser = User.objects.get(id=request.session['uid'])
#         getcart = Cart.objects.filter(User_Id=getuser)

#         ordere = Order.objects.create(
#             User_Id = getuser,
#             cart = getcart,
#         )
#         return redirect("Checkcompl")
#     else:
#         return redirect("index")


# Register User
def U_Register(request):
    try:
        if request.method == 'POST':
            Un = request.POST['Username']
            Fn = request.POST['Fname']
            Ln = request.POST['Lname']
            Em = request.POST['Uemail']
            Ph = request.POST['Uphone']
            Adr1 = request.POST['Uadd1']
            Adr2 = request.POST['Uadd2']
            City = request.POST['UCity']
            State = request.POST['UState']
            pin = request.POST['Upin']
            Pwd = request.POST['Upassword']

            slr = User.objects.create(Username=Un,Ufname=Fn,Ulname=Ln,Uemail=Em,Umobile=Ph,Uaddress1=Adr1,Uaddress2=Adr2,UCity=City,UState=State,UPincode=pin,Upassword=Pwd)
            return redirect("Userlogin")
        else:
            msg = "Method Changes"
            return render(request, "app/user-Register.html",{'err':msg})
    except:
        if request.method == 'POST':
            Un = request.POST['Username']
            Fn = request.POST['Fname']
            Ln = request.POST['Lname']
            Em = request.POST['Uemail']
            Ph = request.POST['Uphone']
            Pwd = request.POST['Upassword']

            slr = User.objects.create(Username=Un,Ufname=Fn,Ulname=Ln,Uemail=Em,Umobile=Ph,Upassword=Pwd)
            return redirect("Userlogin")
        else:
            msg = "Method Changes"
            return render(request, "app/user-Register.html",{'err':msg})

# Login User
def U_login(request):
    try:
        Em = request.POST['Uemail']
        Pwd = request.POST['Upassword']

        usr = User.objects.filter(Uemail=Em)
        us = User.objects.filter(Username=Em)
        if len(usr) > 0:
            if usr[0].Upassword == Pwd:
                request.session['uid']= usr[0].id
                request.session['Fname']= usr[0].Ufname
                request.session['Uemail']= usr[0].Uemail

                return redirect("index")
            else:
                msg = "Password is Incorrect..!"
                return render(request, "app/user-login.html",{'err':msg})
        elif len(us) > 0:
            if us[0].Upassword == Pwd:
                request.session['uid']= us[0].id
                request.session['Fname']= us[0].Ufname
                request.session['Uemail']= us[0].Uemail
                return redirect("index")
            else:
                msg = "Password is Incorrect..!"
                return render(request, "app/user-login.html",{'err':msg})
        else:
            msg = "User Doesn't Found"
            return render(request, "app/user-login.html",{'err':msg})
    except:
        msg = "User Doesn't Found"
        return render(request, "app/user-login.html",{'err':msg})

# User Email sending
def U_Send_OTP(request):
    if request.method == 'POST':
        em = request.POST['email']

        getuser = User.objects.filter(Uemail=em)
        if len(getuser) > 0:
            did = User.objects.get(Uemail=em)
            subject = 'SportMart Forgot Password'
            otp = ''
            for i in range (6):
                otp+=str(randint(1,9))
            did.UOTP = otp
            did.save()
            message = f'Hi {em},\nThank you for Contact to SPORTMART. \n\nYour OTP is {otp}. \n\nContinue & Enjoy To Shopping'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [em, ]
            # send_mail( subject, message, email_from, recipient_list )
            return render(request, "app/user-Enter OTP.html",{'em':em,})
        else:
            msg = "Email is Incorrect..!"
            return render(request, "app/user-Forgot-Password.html",{'err':msg})
    else:
        msg = "Email is Incorrect..!"
        return render(request, "app/user-Forgot-Password.html",{'err':msg})

# User otp verify
def U_OTP_Verify(request):
    if request.method=="POST":
        em = request.POST['email']
        otp2=int(request.POST['Sotp'])
        did = User.objects.get(Uemail=em)
        if did.UOTP==otp2:
            return render(request,"app/user-Recover-Password.html",{'em':em,'otp':did.UOTP})
        else:
            msg="Invaild OTP...!"
            return render(request, "app/user-Enter OTP.html",{'err':msg,'em':em})

# User recover password
def U_Changpassword(request):
    if request.method=="POST":
        em = request.POST['email']
        otp2=int(request.POST['Sotp'])
        pwd = request.POST['password']
        did = User.objects.get(Uemail=em)
        did.Upassword = pwd
        did.save()
        msg = "Great..!\nYour Password is Change"
        return render(request, "app/user-login.html",{'err':msg})

# User change password
def U_Changpasswrd(request):
    if 'uid' in request.session:
        if request.method == "POST":
            paswrd = request.POST['Current']
            npas = request.POST['newped']
            cpass = request.POST['password']
            chngpas = User.objects.get(id=request.session['uid'])
            if chngpas.Upassword == paswrd:
                if npas==cpass:
                    chngpas.Upassword = npas
                    chngpas.save()
                    msg = "Your Password is Change"
                    del request.session['uid']
                    del request.session['Fname']
                    del request.session['Uemail']
                    return render(request, "app/user-login.html",{'err':msg})
                else:
                    msg = "Confirm Password Is Not Same"
                    return render(request, "app/user-changepass.html",{'err':msg})
            else:
                msg = "Current Password Is Wrong"
                return render(request, "app/user-changepass.html",{'err':msg})
        else:
            msg = "Something Wrong"
            return render(request, "app/user-changepass.html",{'err':msg})
    else:
        msg = "Email is Incorrect..!"
        return render(request, "app/user-changepass.html",{'err':msg})

# User Profile Update
def U_Update(request):
    if 'uid' in request.session:
        if request.method == "POST":
            updusr = User.objects.get(id=request.session['uid'])
            updusr.Username = request.POST['Username'] if request.POST['Username'] else updusr.Username
            updusr.Ufname = request.POST['Fname'] if request.POST['Fname'] else updusr.Ufname
            updusr.Ulname = request.POST['Lname'] if request.POST['Lname'] else updusr.Ulname
            updusr.Umobile = request.POST['Uphone'] if request.POST['Uphone'] else updusr.Umobile
            updusr.Uaddress1 = request.POST['Uadd1'] if request.POST['Uadd1'] else updusr.Uaddress1
            updusr.Uaddress2 = request.POST['Uadd2'] if request.POST['Uadd2'] else updusr.Uaddress2
            updusr.UCity = request.POST['UCity'] if request.POST['UCity'] else updusr.UCity
            updusr.UState = request.POST['UState'] if request.POST['UState'] else updusr.UState
            updusr.UPincode = request.POST['Upin'] if request.POST['Upin'] else updusr.UPincode
            updusr.save()
            msg = 'Save Changes'
            return render(request, "app/user-Profile.html",{'err':msg,'user': updusr})
        else:
            msg = 'Method Change'
            return render(request, "app/user-Profile.html",{'err': msg,'user': updusr})
    else:
        return redirect("Userlogin")

# User Logout
def U_Logout(request):
    try:
        del request.session['uid']
        del request.session['Fname']
        del request.session['Uemail']
        return redirect("index")
    except:
        return redirect("index")

# Add To Cart Process
def Add_To_Cart(request,pk):
    if 'uid' in request.session:
        ProductData = Product.objects.get(id=pk)
        getuser = User.objects.get(id=request.session['uid'])

        cart = Cart.objects.create(
            getprod = ProductData,
            User_Id = getuser,
            Total = ProductData.Product_Price,
        )
        return redirect('index')
    else:
        return redirect('Userlogin')

# Item Remove To Cart
def one_remove(request,pk):
    if 'uid' in request.session:
        item = Cart.objects.get(id=pk)
        item.delete()
        return redirect('cart')
    else:
        return redirect('Userlogin')

# Clear Cart
def Cart_remove(request):
    if 'uid' in request.session:
        getuser = User.objects.get(id=request.session['uid'])
        item = Cart.objects.filter(User_Id=getuser)
        item.delete()
        return redirect('cart')
    else:
        return redirect('Userlogin')


# Product Review
def Review_p(request,pk):
    if 'uid' in request.session:
        if request.method == "POST":
            ProductData = Product.objects.get(id=pk)
            getuser = User.objects.get(id=request.session['uid'])
            rate =request.POST['rating']
            text = request.POST['reviews']

            rat = Rating.objects.create(
                getprod = ProductData,
                getuser = getuser,
                rating = rate,
                Review = text,
            )
            return redirect("index")
        else:
            rv = Rating.objects.filter(getprod=ProductData)
            count=rv.count()
            return render(request, "app/User-View-Product.html",{'data':ProductData,'rev':rv,"count":count})
    else:
        return redirect("Userlogin")


# Seller Side Functions

# Page Functions.

# Forgot Page
def S_Forgot_Page(request):
    return render(request, "app/S-Forgot-Password.html")

# Enter Otp page
def S_OTP_page(request):
    return render(request, "app/S-Enter OTP.html")

# Recover Page
def S_recov_Page(request):
    return render(request, "app/S-Recover-Password.html")

# Index Page
def S_IndexPage(request):
    if 'id' in request.session:
        slr = seller.objects.get(id=request.session['id'])
        pro = Product.objects.filter(Seller_ID=slr)
        co = pro.count()
        return render(request,"app/S-index.html",{'slr': slr,'co':co})
    else:
        return redirect("loginpage")
    
# Register Page
def S_RegisterPage(request):
    if 'id' in request.session:
        return redirect('indexpage')
    else:
        return render(request, "app/S-Reg.html")

# Login page
def S_Loginpage(request):
    if 'id' in request.session:
        return redirect('indexpage')
    else:
        return render(request, "app/S-Login.html")

# Chang password Page
def S_changpasspage(request):
    if 'id' in request.session:
        slr = seller.objects.get(id=request.session['id'])
        return render(request, "app/S-Changepass.html",{'slr': slr})
    else:
        return redirect("loginpage")

# All Product Page
def S_All_Product_Page(request):
    if 'id' in request.session:
        sel=seller.objects.get(id=request.session['id'])
        getProductData = Product.objects.filter(Seller_ID=sel)
        return render(request, "app/S-All-product.html",{'data':getProductData,'slr': sel})
    else:
        return redirect("loginpage")

# Add Product Page
def S_Add_Product_Page(request):
    if 'id' in request.session:
        slr = seller.objects.get(id=request.session['id'])
        return render(request, "app/S-Add-Product.html",{'slr': slr})
    else:
        return redirect("loginpage")

# Order Page
def S_Orderpage(request):
    if 'id' in request.session:
        slr = seller.objects.get(id=request.session['id'])
        return render(request, "app/S-Orderpage.html",{'slr': slr})
    else:
        return redirect("loginpage")

# Seller Profile Page
def S_Profile(request):
    if 'id' in request.session:
        getslr = seller.objects.get(id=request.session['id'])
        return render(request, "app/S-Profile.html",{'slr': getslr})
    else:
        return redirect("loginpage")

# Order Action page
def S_Action(request):
    if 'id' in request.session:
        slr = seller.objects.get(id=request.session['id'])
        return render(request, "app/S-Action.html",{'slr': slr})
    else:
        return redirect("loginpage")    

# ShowPage
def S_View_Product_Page(request,pk):
    if 'id' in request.session:
        ProductData = Product.objects.get(id=pk)
        slr = seller.objects.get(id=request.session['id'])
        rv = Rating.objects.filter(getprod=ProductData)
        count=rv.count()
        return render(request, "app/S-View_Product.html",{'data':ProductData,'slr':slr,'rev':rv,"count":count,})
    else:
        return redirect("loginpage")

# View Product
def S_Pro_Edit_page(request,pk):
    if 'id' in request.session:
        slr = seller.objects.get(id=request.session['id'])
        ProductData = Product.objects.get(id=pk)
        rv = Rating.objects.filter(getprod=ProductData)
        count=rv.count()
        return render(request, "app/S-Edit-Product.html",{'data':ProductData,'rev':rv,"count":count,'slr':slr})
    else:
        return redirect("loginpage") 

# Method Functions.

# Register Seller
def S_Registeruser(request):
    try:
        if request.method == 'POST':
            un = request.POST['username']
            sn = request.POST['sname']
            shn = request.POST['shopname']
            em = request.POST['email']
            ph = request.POST['phone']
            adr1 = request.POST['add1']
            adr2 = request.POST['add2']
            city = request.POST['City']
            state = request.POST['State']
            pincode = request.POST['pin']
            pwd = request.POST['password']

            slr = seller.objects.create(username=un,Sname=sn,shop_name=shn,email=em,mobile=ph,address1 = adr1,address2 = adr2,City = city,state = state,Pincode = pincode,password=pwd)
            return redirect("loginpage")
        else:
            msg = "Method Changes"
            return render(request, "app/S-Reg.html",{'err':msg})
    except:
        if request.method == 'POST':
            un = request.POST['username']
            sn = request.POST['sname']
            shn = request.POST['shopname']
            em = request.POST['email']
            ph = request.POST['phone']
            city = request.POST['City']
            state = request.POST['State']
            pwd = request.POST['password']

            slr = seller.objects.create(username=un,Sname=sn,shop_name=shn,email=em,mobile=ph,City = city,state = state,password=pwd)
            return redirect("loginpage")
        else:
            msg = "Method Changes"
            return render(request, "app/S-Reg.html",{'err':msg})

# Login Seller
def S_Loginuser(request):
    try:
        em = request.POST['email']
        pwd = request.POST['password']

        user = seller.objects.filter(email=em)
        if len(user) > 0:
            if user[0].password == pwd:
                request.session['id']= user[0].id
                request.session['Sname']= user[0].Sname
                request.session['email']= user[0].email

                return redirect("indexpage")
            else:
                msg = "Password is Incorrect..!"
                return render(request, "app/S-Login.html",{'err':msg})
        else:
            msg = "Seller Doesn't Found"
            return render(request, "app/S-Login.html",{'err':msg})
    except:
        msg = "Sever Slow Please Try Again...."
        return render(request, "app/S-Login.html",{'err':msg})

# Email Send
def S_Send_OTP(request):
    try:
        if request.method == 'POST':
            em = request.POST['email']

            user = seller.objects.filter(email=em)
            if len(user) > 0:
                did = seller.objects.get(email=em)
                subject = 'SportMart Seller Forgot Password'
                otp = ''
                for i in range (6):
                    otp+=str(randint(1,9))
                did.OTP = otp
                did.save()
                message = f'Hi {em},\nThank you for Contact to SPORTMART. \nYour OTP is {otp}.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [em, ]
                # send_mail( subject, message, email_from, recipient_list )
                return render(request, "app/S-Enter OTP.html",{'em':em,})
            else:
                msg = "Email is Incorrect..!"
                return render(request, "app/S-Forgot-Password.html",{'err':msg})
        else:
            msg = "Email is Incorrect..!"
            return render(request, "app/S-Forgot-Password.html",{'err':msg})
    except:
        msg = "Sever Is Slow Please Try Again Later....."
        return render(request, "app/S-Forgot-Password.html",{'err':msg})

# Otp Verify
def S_OTP_Verify(request):
    try:
        if request.method=="POST":
            em = request.POST['email']
            otp2=int(request.POST['Sotp'])
            did = seller.objects.get(email=em)
            if did.OTP==otp2:
                return render(request,"app/S-Recover-Password.html",{'em':em,'otp':did.OTP})
            else:
                msg="Invaild OTP...!"
                return render(request, "app/S-Enter OTP.html",{'err':msg,'em':em})
    except:
        return redirect('VerifyotpS')

# Recover Password
def S_Changpassword(request):
    try:
        if request.method=="POST":
            em = request.POST['email']
            otp2=int(request.POST['Sotp'])
            pwd = request.POST['password']
            did = seller.objects.get(email=em)
            did.password = pwd
            did.save()
            msg = "Great..!\nYour Password is Change"
            return render(request, "app/S-Login.html",{'err':msg})
    except:
        return redirect('recoverpassword')

# Seller LogOut
def S_logOut(request):
    try:
        del request.session['id']
        del request.session['Sname']
        del request.session['email']
        return redirect("loginpage")
    except:
        return redirect("loginpage")

# Add Product
def S_addProduct(request):
    if 'id' in request.session:
        if request.method == 'POST':
            pname = request.POST['pname']
            ptitle = request.POST['ptitle']
            Pimage = request.FILES['pimage']
            pcate = request.POST['pcat']
            pprice = float(request.POST['pprice'])
            pmrp = float(request.POST['pMRP'])
            
            category = Category.objects.get(pcategory=pcate)
            sel=seller.objects.get(id=request.session['id'])

            product = Product.objects.create(
                Seller_ID = sel,
                Product_Name = pname,
                Product_Title = ptitle,
                Product_Image = Pimage,
                Product_Category = category,
                Product_Price = pprice,
                Product_MRP = pmrp
            )
            return redirect("allProductpage")
        else:
            return redirect("addproductpage")
    else:
        return redirect("loginpage")

# Chang Password
def S_Changpasswrd(request):
    if 'id' in request.session:
        chngpas = seller.objects.get(id=request.session['id'])
        if request.method == "POST":
            paswrd = request.POST['Current']
            npas = request.POST['newped']
            cpass = request.POST['cpassword']
            if chngpas.password == paswrd:
                if npas==cpass:
                    chngpas.password = npas
                    chngpas.save()
                    msg = "Your Password is Change"
                    del request.session['id']
                    del request.session['Sname']
                    del request.session['email']
                    return render(request, "app/S-Login.html",{'err':msg,'slr':chngpas})
                else:
                    msg = "Confirm Password Is Not Same"
                    return render(request, "app/S-Changepass.html",{'err':msg,'slr':chngpas})
            else:
                msg = "Current Password Is Wrong"
                return render(request, "app/S-Changepass.html",{'err':msg,'slr':chngpas})
        else:
            return render(request, "app/S-Changepass.html",{'slr':chngpas})
    else:
        return redirect("loginpage")

# Delete Product
def Deletepage(request,pk):
    try:
        if 'id' in request.session:
            ProductData = Product.objects.get(id=pk)
            ProductData.delete()
            return redirect("allProductpage")
        else:
            return redirect("loginpage")
    except:
        return redirect("allProductpage")

# Image Upload
def Uploadimage(request,pk):
    try:
        if 'id' in request.session:
            slr = seller.objects.get(id=request.session['id'])
            ProductData = Product.objects.get(id=pk)
            rv = Rating.objects.filter(getprod=ProductData)
            count=rv.count()
            ProductData.Product_Image = request.FILES['pimage'] if request.FILES['pimage'] else ProductData.Product_Image
            ProductData.save()
            return render(request, "app/S-View_Product.html",{'pk':pk,'data':ProductData,'rev':rv,"count":count,'slr':slr})
        else:
            return redirect("loginpage")
    except:
        return redirect('showprod')

def Update_pro(request,pk):
    try:
        if 'id' in request.session:
            slr = seller.objects.get(id=request.session['id'])
            ProductData = Product.objects.get(id=pk)
            ProductData.Product_Name = request.POST['pname'] if request.POST['pname'] else ProductData.Product_Name
            ProductData.Product_Title = request.POST['ptitle'] if request.POST['ptitle'] else ProductData.Product_Title
            ProductData.Product_Price = float(request.POST['pprice']) if float(request.POST['pprice']) else ProductData.Product_Price
            ProductData.Product_MRP = float(request.POST['pMRP']) if float(request.POST['pMRP']) else ProductData.Product_MRP
            try:
                cat = request.POST['pcat']
                category = Category.objects.get(pcategory=cat)
                ProductData.Product_Category = category if category else cat        
            except:
                ProductData.Product_Category = ProductData.Product_Category
            ProductData.save()
            return render(request, "app/S-View_Product.html",{'pk':pk,'data':ProductData,'slr':slr})
        else:
            return redirect("loginpage")
    except:
        return redirect('showprod')

# Update Seller Profile
def S_Update(request):
    try:
        if 'id' in request.session:
            if request.method == "POST":
                updsel = seller.objects.get(id=request.session['id'])
                updsel.username = request.POST['username'] if request.POST['username'] else updsel.username
                updsel.Sname = request.POST['sname'] if request.POST['sname'] else updsel.Sname
                updsel.shop_name = request.POST['shopname'] if request.POST['shopname'] else updsel.shop_name
                updsel.mobile = request.POST['phone'] if request.POST['phone'] else updsel.mobile
                updsel.address1 = request.POST['add1'] if request.POST['add1'] else updsel.address1
                updsel.address2 = request.POST['add2'] if request.POST['add2'] else updsel.address2
                updsel.City = request.POST['City'] if request.POST['City'] else updsel.City
                updsel.state = request.POST['State'] if request.POST['State'] else updsel.state
                updsel.Pincode = request.POST['pin'] if request.POST['pin'] else updsel.Pincode
                updsel.save()
                msg = 'Save Changes'
                return render(request, "app/S-Profile.html",{'err':msg,'slr': updsel})
            else:
                msg = 'Method Change'
                return render(request, "app/S-Profile.html",{'err': msg,'slr': updsel})
        else:
            return redirect("loginpage")
    except:
        return redirect("Sprofile")

