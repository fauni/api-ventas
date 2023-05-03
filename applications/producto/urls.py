from django.urls import path

from . import views

app_name = 'producto_app'

urlpatterns = [
    path(
        "api/estado/lista", 
        views.EstadoListApiView.as_view(), 
        name="estados"
    ),
    path(
        "api/estado/create", 
        views.EstadoCreateView.as_view(), 
    ),
    path(
        "api/almacen/lista", 
        views.AlmacenListApiView.as_view(), 
        name="almacenes"
    ),
    path(
        'api/almacen/detail/<pk>', 
        views.AlmacenDetailView.as_view(),
        name='almacen'
    ),
    path(
        "api/almacen/create", 
        views.AlmacenCreateView.as_view(), 
    ),
    path(
        'api/almacen/delete/<pk>', 
        views.AlmacenDeleteView.as_view(),
    ),
    path(
        'api/almacen/update/<pk>', 
        views.AlmacenUpdateView.as_view(),
    ),
    #############    Producto   #####################
    path(
        "api/producto/lista", 
        views.ProductoListApiView.as_view(), 
        name="productos"
    ),
    path(
        'api/producto/detail/<pk>', 
        views.ProductoDetailView.as_view(),
        name='producto'
    ),
    path(
        "api/producto/create", 
        views.ProductoCreateView.as_view(), 
    ),
    path(
        'api/producto/delete/<pk>', 
        views.ProductoDeleteView.as_view(),
    ),
    path(
        'api/almacen/update/<pk>', 
        views.ProductoUpdateView.as_view(),
    ),
    #############     MOVIMIENTO STOCK     #################
    path(
        "api/movimientostock/lista", 
        views.MovimientoStockListAiView.as_view(), 
        name="productos"
    ),
    path(
        "api/movimientostock/create", 
        views.MovimientoStockCreateView.as_view(), 
    ),
    path(
        "api/movimientostocklote/create", 
        views.MovimientoStockLoteCreateView.as_view(), 
    ),
]