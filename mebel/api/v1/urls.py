from django.urls import path

from api.v1.dashboard.user.views import RegisterView, LoginView, LogOutview
from api.v1.sayt.Category.views import CategoryView
from api.v1.sayt.Product.views import ProductView

urlpatterns = [
    path('ctg/list/', CategoryView.as_view(), name='ctg_list'),
    path('ctg/list/<int:pk>/', CategoryView.as_view(), name='ctg_one'),


    path('pro/list/', ProductView.as_view(), name='pro_list'),
    path('pro/list/<int:pk>/', ProductView.as_view(), name='pro_one'),


    path('auth/register/', RegisterView.as_view(), name="api_dash_register"),
    path('auth/login/', LoginView.as_view(), name="api_dash_loginview"),
    path('auth/loginout/', LogOutview.as_view(), name="api_dash_logout")

]



