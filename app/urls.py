from django.urls import path
from . import views

urlpatterns = [
    path('',views.productos_list),
    path('index',views.index, name='index'),
    path('productos_del/<id_producto>',views.productos_del,name='productos_del'),
    path('productos_edit/<id_producto>',views.productos_edit,name='productos_edit'),
    path('productos_edit_form',views.editar_producto_form,name='productos_edit_form'),
    path('productos_list',views.productos_list,name='productos_list'),
    path('productos_add',views.productos_add,name='productos_add'),
    path('productos_add_vistas',views.productos_add_vistas, name='productos_add_vistas'),
    path('home', views.cargar_home)
]
