from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    # path("pay/",views.indexa,name="indef"),
    path('',views.login,name='login'),
    path('Admin-Home/',views.index,name='Aindex'),
    path('Admin-All-Users/',views.A_User,name='AUsers'),
    path('Admin-All-Sellers/',views.A_seller,name='Aseller'),
    path('Admin-All-Products/',views.A_Products,name='Aproduct'),
    path('Admin-All-Category/',views.A_Category,name='Acat'),
    path('Admin-Orders/',views.A_Order,name='Aorder'),
    path('Admin-User-Rating/',views.A_Rat,name='Arat'),

    path('Admin-Login/',views.A_login,name='log'),
    path('Admin-LogOut/',views.A_logout,name='logout'),
    path('Admin-Add-Category/',views.A_A_Category,name='addcat'),

    path('Admin-User-Delete/<int:pk> /',views.del_User,name='Adelusr'),
    path('Admin-Seller-Delete/<int:pk> /',views.del_Seller,name='Adelsel'),
    path('Admin-Product-Delete/<int:pk> /',views.del_Product,name='Adelpro'),
    path('Admin-Category-Delete/<int:pk> /',views.del_Category,name='Adelcat'),
    path('Admin-Rating-Delete/<int:pk> /',views.del_Rating,name='Adelrat'),

]