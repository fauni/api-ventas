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
        'api/producto/update/<pk>',
        views.ProductoUpdateView.as_view(),
    ),
    #############     PRODUCTO LOTE       #################
    path(
        'api/producto-lote/lista/<kword>/',
        views.ProductoLoteListApiView.as_view(),
    ),

    #############     PRODUCTO BATCH       #################
    path(
        'api/producto-batch/lista/<kword>/',
        views.ProductoBatchListApiView.as_view(),
    ),

    #############     TIPO DE MOVIMIENTO      #################
    path(
        "api/tipo-movimiento/lista",
        views.TipoMovimientoListApiView.as_view(),
        name="tipomovimientos"
    ),

    #############       stock       ###################
    path(
        "api/stock/lista",
        views.StockListApiView.as_view(),
    ),
    path(
        "api/stock-lote/lista",
        views.StockLoteListApiView.as_view(),
    ),

    #############     MOVIMIENTO STOCK     #################
    path(
        "api/movimientostock/lista",
        views.MovimientoStockListApiView.as_view(),
        name="movimientostock"
    ),
    path(
        "api/movimientostock/almacen/<kword>/",
        views.MovimientoStockAlmacenListApiView.as_view(),
        name="movimientostockalmacen"
    ),
    path(
        "api/movimientostock/producto/<kword>/",
        views.MovimientoStockProductoListApiView.as_view(),
        name="movimientostockalmacen"
    ),
    path(
        "api/movimientostock/create", 
        views.MovimientoStockCreateView.as_view(), 
    ),
    path(
        "api/movimientostocklote/create", 
        views.MovimientoStockLoteCreateView.as_view(), 
    ),

    #############    Categoria   #####################
    path(
        "api/categoria/lista",
        views.CategoriaListApiView.as_view(),
        name="categorias"
    ),
    path(
        "api/categoria/create",
        views.CategoriaCreateView.as_view(),
    ),
    path(
        'api/categoria/detail/<pk>',
        views.CategoriaDetailView.as_view(),
        name='categoria'
    ),
    path(
        'api/categoria/delete/<pk>',
        views.CategoriaDeleteView.as_view(),
    ),
    path(
        'api/categoria/update/<pk>',
        views.CategoriaUpdateView.as_view(),
    ),

    #############    Grupos   #####################
    path(
        "api/grupo/lista",
        views.GrupoListApiView.as_view(),
        name="grupos"
    ),
    path(
        "api/grupo/create",
        views.GrupoCreateView.as_view(),
    ),
    path(
        'api/grupo/detail/<pk>',
        views.GrupoDetailView.as_view(),
        name='grupo'
    ),
    path(
        'api/grupo/delete/<pk>',
        views.GrupoDeleteView.as_view(),
    ),
    path(
        'api/grupo/update/<pk>',
        views.GrupoUpdateView.as_view(),
    ),

    #############    Proveedor   #####################
    path(
        "api/proveedor/lista",
        views.ProveedorListApiView.as_view(),
        name="proveedores"
    ),
    path(
        "api/proveedor/create",
        views.ProveedorCreateView.as_view(),
    ),
    path(
        'api/proveedor/detail/<pk>',
        views.ProveedorDetailView.as_view(),
        name='proveedor'
    ),
    path(
        'api/proveedor/delete/<pk>',
        views.ProveedorDeleteView.as_view(),
    ),
    path(
        'api/proveedor/update/<pk>',
        views.ProveedorUpdateView.as_view(),
    ),
]