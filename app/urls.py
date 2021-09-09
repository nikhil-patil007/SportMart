from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
# User Site Path

# User site Page path
    path('',views.U_Indexpage,name='index'),
    path('User-Login/',views.U_Loginpage,name='Userlogin'),
    path('User-RegisterPage/',views.U_Registerpage,name='UregisterPage'),
    path('User-Cart/',views.U_Cart,name="cart"),
    path('User-Profile/',views.U_Profile,name='Uprofile'),
    path('User-ChangePassword-page/',views.U_Changepaspage,name='Uchang'),
    path('User-Order-Page/',views.U_Orderpage,name="Uorder"),
    path('User-Order-Tracking/',views.U_Trackpage,name="track"),
    path('User-Order-Complete/',views.Completpage,name='Checkcompl'),
    path("User-ForgotPassword/",views.U_Forgot_Page,name="Uforgotpassword"),
    path("User-OTP-Verify/",views.U_OTP_page,name="Verifyotpu"),
    path("User-RecoverPassword/",views.U_recov_Page,name="Urecoverpaswrd"),

# User site function path
    path('User-RegisterUser/',views.U_Register,name='Ureguser'),
    path('User-Login-User/',views.U_login,name="loginuser"),
    path('User-Send-Otp/',views.U_Send_OTP,name='otp'),
    path('User-Otp-enter/',views.U_OTP_Verify,name='enterotp'),
    path('User-Password-enter/',views.U_Changpassword,name='enterpaas'),
    path('User-Change-pass/',views.U_Changpasswrd,name="changpasU"),
    path('User-Logout/',views.U_Logout,name="ULogout"),
    path('User-Update/',views.U_Update,name='usrupdate'),
    path('User-Update-Cart/',views.qty,name='cartupdate'),

# User Site With Primary Key
    path("User-Show-Product/<int:pk>/",views.U_showpage,name='ushowprd'),
    path('User-Add-Cart/<int:pk>/',views.Add_To_Cart,name='Add_To_Cart'),
    path('User-Item-Remove/<int:pk>/',views.one_remove,name='removeitem'),
    path('User-Cart-Remove/<int:pk>/',views.Cart_remove,name='removeCart'),
    
# Seller Site Paths
# Seller site page path
    path("seller/",views.S_Loginpage,name="loginpage"),
    path("seller-RegisterPage/",views.S_RegisterPage,name="registerpage"),
    path("seller-IndexPage/",views.S_IndexPage,name="indexpage"),
    path("seller-All-Product/",views.S_All_Product_Page,name="allProductpage"),
    path("seller-Add-Product/",views.S_Add_Product_Page,name="addproductpage"),
    path("seller-ForgotPassword/",views.S_Forgot_Page,name="forgotpassword"),
    path("seller-OTP-Verify/",views.S_OTP_page,name="VerifyotpS"),
    path("seller-RecoverPassword/",views.S_recov_Page,name="recoverpassword"),
    path("Seller-Profile/",views.S_Profile,name="Sprofile"),
    path("Seller-Changepassword-Page/",views.S_changpasspage,name="Schang"),
    path("Seller-Order-Page/",views.S_Orderpage,name="Sorder"),
    path("Seller-Actions-Page/",views.S_Action,name="Action"),

# Seller site function path
    path("seller-Forgot-Password/",views.S_Send_OTP,name="Sotpsent"),
    path("seller-Enter-otp/",views.S_OTP_Verify,name="SOTPVERIFY"),
    path("seller-Change-Pass/",views.S_Changpassword,name="Snewpass"),
    path("seller-RegisterUser/",views.S_Registeruser,name="registerseller"),
    path("seller-LoginUser/",views.S_Loginuser,name="loginseller"),
    path("seller-Add-Product-User/",views.S_addProduct,name="addpro"),
    path("seller-ChangePassword/",views.S_Changpasswrd,name="Schang"),
    path("seller-LogOut/",views.S_logOut,name="S_LogOut"),
    path('seller-Update/',views.S_Update,name='slrupdate'),

# Seller Site With Primary key 
    path("Seller-Delete-Product/<int:pk>/",views.Deletepage,name="deleteprod"),
    path("Seller-Edit-Product/<int:pk>/",views.S_Pro_Edit_page,name='editPro'),
    path("Seller-View-Product/<int:pk>/",views.S_View_Product_Page,name="showprod"),
    path("Seller-Upload-Image/<int:pk>/",views.Uploadimage,name="upload"),
    path("Seller-Update-Product/<int:pk>/",views.Update_pro,name="UpdatePro"),
    path("User-Review/<int:pk>/",views.Review_p,name='review'),

]