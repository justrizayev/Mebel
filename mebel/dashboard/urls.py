from django.urls import path

from dashboard.Product.views import *
from dashboard.views import *
from dashboard.Category.views import *

urlpatterns = [
    path('ctg/list/', ctg_list, name='dashboard-ctg-list'),
    path('ctg/detail/<int:pk>/', ctg_detail, name='dashboard-ctg-detail'),
    path('ctg/delete/<int:pk>/', ctg_delete, name='dashboard-ctg-delete'),
    path('ctg/add/', ctg_add, name='dashboard-ctg-add'),
    path('ctg/edit/<int:pk>/', ctg_edit, name='dashboard-ctg-edit'),
    path('ctg/confirm/<int:pk>/', ctg_confirm, name='dashboard-ctg-confirm'),

    path('pro/confirm/<int:pk>/', pro_confirm, name='dashboard-pro-confirm'),
    path('pro/list/', pro_list, name='dashboard-pro-list'),
    path('pro/detail/<int:pk>/', pro_detail, name='dashboard-pro-detail'),
    path('pro/delete/<int:pk>/', pro_delete, name='dashboard-pro-delete'),
    path('pro/edit/<int:pk>/', pro_edit, name='dashboard-pro-edit'),
    path('pro/add/', product_add, name='dashboard-pro-add'),


    path('', index, name='dashboard'),
    path('login/', dash_login, name='dashboard_login'),
    path('logout/', dash_logout, name='dashboard_logout'),
    path('register/', dash_register, name='dashboard_register'),

]
