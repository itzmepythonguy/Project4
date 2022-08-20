from . import views
from django.urls import path

app_name='cart'

urlpatterns=[
    path('add/<int:pro_id>/',views.add_cart,name='add_cart'),
    path('',views.cartdetail,name='cartdetail'),
    path('remove/<int:pro_id>/',views.remove,name='remove'),
    path('delete/<int:pro_id>/',views.delete,name='delete'),
]