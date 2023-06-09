from drf_writable_nested import WritableNestedModelSerializer

from rest_framework import serializers, pagination


from .models import (
    Estado,
    Almacen,
    Producto,
    Categoria,
    TipoMovimiento,
    Grupo,
    Proveedor,
    ProductoLote,
    ProductoStock,
    MovimientoStock,
    ProductoBatch
)

# Tipo de Movimiento
class TipoMovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMovimiento
        fields = ('__all__')

# Estado

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ('__all__')

# Categoria Serializer
class CategoriaSerializer(serializers.ModelSerializer):
    estado = EstadoSerializer()
    class Meta:
        model = Categoria
        fields = ('__all__')

class CategoriaCreateSerializer(serializers.ModelSerializer):
    # estado = EstadoSerializer()
    class Meta:
        model = Categoria
        fields = ('__all__')

# Grupo Serializer
class GrupoCreateSerializer(serializers.ModelSerializer):
    # estado = EstadoSerializer()
    class Meta:
        model = Grupo
        fields = ('__all__')

class GrupoSerializer(serializers.ModelSerializer):
    estado = EstadoSerializer()
    class Meta:
        model = Grupo
        fields = ('__all__')

# Provider Serializer
class ProveedorSerializer(serializers.ModelSerializer):
    estado = EstadoSerializer()
    class Meta:
        model = Proveedor
        fields = ('__all__')

class ProveedorCreateSerializer(serializers.ModelSerializer):
    # estado = EstadoSerializer()
    class Meta:
        model = Proveedor
        fields = ('__all__')
        
# Almacen
class AlmacenCreateSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Almacen
        fields = ('__all__')

class AlmacenSerializer(WritableNestedModelSerializer,
                        serializers.ModelSerializer):
    estado = EstadoSerializer()
    class Meta:
        model = Almacen
        fields = (
            'id',
            'nombre',
            'descripcion',
            'lugar',
            'direccion',
            'estado',
        )

# Producto

class ProductoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()
    grupo = GrupoSerializer()
    proveedor = ProveedorSerializer()
    estado = EstadoSerializer()
    class Meta:
        model = Producto
        fields = (
            'id',
            'created',
            'modified',
            'codigo',
            'codigo_barras',
            'nombre',
            'descripcion',
            'unidad',
            'imagen_url',
            'usa_inventarios',
            'usa_lotes',
            'stock',
            'stock_minimo',
            'precio_compra',
            'precio_venta',
            'categoria',
            'grupo',
            'proveedor',
            'estado'
        )

class ProductoMovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = (
            'id',
            'codigo',
            'nombre',
            'descripcion',
            'imagen_url',
            'stock',
            'stock_minimo'
        )
class ProductoCreateSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('__all__')

# Producto Stock ####
class ProductoStockSerializer(serializers.ModelSerializer):
    producto = ProductoMovimientoSerializer()
    almacen = AlmacenSerializer()
    class Meta:
        model = ProductoStock
        fields = (
            'fecha',
            'producto',
            'almacen',
            'valor'
        )

# Producto Batch ####
class ProductoBatchSerializer(serializers.ModelSerializer):
    producto_stock = ProductoStockSerializer()
    class Meta:
        model = ProductoBatch
        fields = (
            'fecha',
            'producto_stock',
            'fecha_vencimiento',
            'fecha_limite_venta',
            'lote',
            'valor'
        )

# Producto Lote ####
class ProductoLoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoLote
        fields = ('__all__')

# Movimiento de Stock   ####
# class MovimientoStockCreateSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = MovimientoStock
#        fields = (
#            'fecha',
#            'producto',
#            'lote',
#            'almacen',
#            'valor',
#            'precio',
#            'descripcion',
#            'tipo_movimiento'
#        )

class MovimientoSerializer(serializers.ModelSerializer):
    producto = ProductoMovimientoSerializer()
    almacen = AlmacenSerializer()
    tipo_movimiento = TipoMovimientoSerializer()
    class Meta:
        model = MovimientoStock
        fields = (
            'fecha',
            'producto',
            'lote',
            'almacen',
            'valor',
            'precio',
            'descripcion',
            'tipo_movimiento',
        )

class MovimientoStockLoteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovimientoStock
        fields = (
            'fecha',
            'producto',
            'lote',
            'almacen',
            'valor',
            'precio',
            'descripcion',
            'fecha_vencimiento',
            'fecha_limite_venta',
            'tipo_movimiento'
        )

class MovimientoStockCreateSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if data['valor']  <= 0:
            raise serializers.ValidationError("La cantidad no puede ser menor o igual a cero")
        if data['precio']  < 10:
            raise serializers.ValidationError("El precio debe ser mayor a 10")
        if data['producto'].usa_lotes == True:
            raise serializers.ValidationError("Este producto necesita tener un número de lote")
        return data

    class Meta:
        model = MovimientoStock
        fields = (
            'fecha',
            'producto',
            'almacen',
            'valor',
            'precio',
            'descripcion',
            'tipo_movimiento'
        )
