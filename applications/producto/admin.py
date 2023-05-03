from django.contrib import admin

from .models import (
    Estado,
    Almacen,
    TipoMovimiento,
    Categoria,
    Grupo,
    Proveedor,
    Producto,
    ProductoLote,
    ProductoStock,
    MovimientoStock
)

# Register your models here.

admin.site.register(Estado)
admin.site.register(Almacen)
admin.site.register(TipoMovimiento)
admin.site.register(Categoria)
admin.site.register(Grupo)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(ProductoLote)
admin.site.register(ProductoStock)
admin.site.register(MovimientoStock)