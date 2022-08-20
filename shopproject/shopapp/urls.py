from .import views
from django.urls import path
app_name='shop'


urlpatterns = [



    path('',views.allproducts,name='allproducts'),
    path('<slug:c_slug>/',views.allproducts,name='allcategory'),
    path('<slug:c_slug>/<slug:pr_slug>/',views.productdet,name='productdet'),
]