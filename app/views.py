from django.shortcuts import render, redirect
from .models import Producto
from django.contrib import messages

# Create your views here.

def index(request):
    productos = Producto.objects.all()
    context ={"productos": productos}
    return render(request,'app/index.html',context )

def productos_del(request,id_producto):
    productos = Producto.objects.get(id_producto=id_producto)
    context ={"productos": productos}
    productos.delete()
    return redirect('productos_list')

def productos_edit(request,id_producto):
    productos = Producto.objects.get(id_producto=id_producto)
    context ={"prod": productos}
    return render(request,'app/productos_edit.html',context )

def productos_list(request):
    productos = Producto.objects.all()
    context ={"productos": productos}
    return render(request,'app/productos_list.html',context )

def productos_add(request):
    v_id_producto = request.POST['txtid']
    nombre_producto = request.POST['txtnombre']
    fecha_vencimiento = request.POST['txtfecha']
    cantidad_producto = request.POST['txtcantidad']
    Marca = request.POST['txtMarca']
    activo = request.POST['txtactivo']
    if v_id_producto == ''or nombre_producto ==''or fecha_vencimiento == ''or cantidad_producto == ''or Marca == ''or activo == '':
        messages.warning(request, 'Se intento agregar sin rellenar los campos')
        return redirect('productos_add_vistas')
    else:
        messages.success(request,'.')
        Producto.objects.create(id_producto= v_id_producto,
                                nombre_producto=nombre_producto,
                                fecha_vencimiento=fecha_vencimiento,
                                cantidad_producto=cantidad_producto,
                                Marca=Marca,
                                activo=activo)
    
    return redirect('productos_add_vistas' )
    
def productos_add_vistas(request):
    productos = Producto.objects.all()
    context ={"productos": productos}
    return render(request,'app/productos_add.html',context )

def crud(request):
    productos = Producto.objects.all()
    context ={"productos": productos}
    return render(request,'app/crud.html',context )

def editar_producto_form(request):
    if request.method == 'POST':
        try:
            v_id_producto = request.POST['txtid']
            productobd = Producto.objects.get(id_producto=v_id_producto)
            nombre_producto = request.POST['txtnombre']
            fecha_vencimiento = request.POST['txtfecha']
            cantidad_producto = request.POST['txtcantidad']
            Marca = request.POST['txtMarca']
            activo = request.POST['txtactivo']

            productobd.nombre_producto = nombre_producto
            productobd.fecha_vencimiento = fecha_vencimiento
            productobd.cantidad_producto = cantidad_producto
            productobd.Marca = Marca
            productobd.activo = activo

            productobd.save()
            return redirect('/')
        except Exception as e:
            print("Error:", e)
            return redirect('/productos_edit/' + v_id_producto)
    else:
        return redirect('/')
    

def cargar_home(request):
    return render(request,'app/home.html')