from django.urls import path

from django.conf.urls import include, url

from .views import (
    my_detail_product,
    lista_products,
    list_products,
    create_product,
    update_product,
    delete_product,
    detail_product
    ,favourite_products,
    products_favourite_list
)


urlpatterns = [
    path('lista/', lista_products, name='lista_products'),
    path('list/<int:userId>/', list_products, name='list_products'),
    path('new/<int:userId>/', create_product, name='create_products'),
    path('update/<int:productId>/', update_product, name='update_product'),
    path('delete/<int:productId>/', delete_product, name='delete_product'),
    
    path('detail/<int:id>/', detail_product, name='detail_product'),

    
    #url(r'(?P<id>\d+)/favourite_products/$', favourite_products, name='favourite_products'),
    
    #path('<int:id>/favourite_products/', favourite_products, name='favourite_products'),
    path('favourite_products/<int:id>/', favourite_products, name='favourite_products'),
  

    path('favoritos/', products_favourite_list, name='products_favourite_list'),
    
    path('mydetail/<int:productId>/', my_detail_product, name='my_detail_product'),

    path('favoritos/', products_favourite_list, name='products_favourite_list'),
]
