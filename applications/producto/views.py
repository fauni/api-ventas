from django.shortcuts import render

from django.views.generic import ListView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

#API
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView
)

# models
from .models import (
    Almacen,
    Estado,
    Producto,
    ProductoLote,
    ProductoStock,
    ProductoBatch,
    MovimientoStock,
    Categoria,
    Grupo,
    Proveedor,
    TipoMovimiento,
)

# serializers
from .serializers import (
    EstadoSerializer,
    AlmacenSerializer,
    AlmacenCreateSeralizer,
    ProductoCreateSeralizer,
    ProductoSerializer,
    MovimientoSerializer,
    MovimientoStockCreateSerializer,
    MovimientoStockLoteCreateSerializer,
    TipoMovimientoSerializer,
    CategoriaSerializer,
    CategoriaCreateSerializer,
    GrupoSerializer,
    GrupoCreateSerializer,
    ProveedorSerializer,
    ProveedorCreateSerializer,
    ProductoLoteSerializer,
    ProductoStockSerializer,
    ProductoBatchSerializer,
    ProductoMovimientoSerializer
)

# ------------- Estado

class EstadoListApiView(ListAPIView):
    serializer_class = EstadoSerializer
    def get_queryset(self):
        return Estado.objects.all()

class EstadoCreateView(CreateAPIView):
    serializer_class = EstadoSerializer

# ------------- Almacen
class AlmacenListApiView(ListAPIView):
    serializer_class = AlmacenSerializer
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        return Almacen.objects.all()

class AlmacenDetailView(RetrieveAPIView):
    serializer_class = AlmacenSerializer
    queryset = Almacen.objects.filter()

class AlmacenCreateView(CreateAPIView):
    serializer_class = AlmacenCreateSeralizer

class AlmacenDeleteView(DestroyAPIView):
    serializer_class = AlmacenCreateSeralizer
    queryset = Almacen.objects.all()

class AlmacenUpdateView(UpdateAPIView):
    serializer_class = AlmacenCreateSeralizer
    queryset = Almacen.objects.all()

##############      PRODUCTO LOTE VIEWS      #########################
class ProductoLoteListApiView(ListAPIView):
    serializer_class = ProductoLoteSerializer
    def get_queryset(self):
        kword = self.kwargs['kword']
        return ProductoLote.objects.filter(
            producto = kword
        )

##############      PRODUCTO BATCH VIEW      #########################
class ProductoBatchListApiView(ListAPIView):
    serializer_class = ProductoBatchSerializer
    def get_queryset(self):
        kword = self.kwargs['kword']
        return ProductoBatch.objects.filter(
            producto_stock__producto = kword
        )

##############      PRODUCTO VIEWS      #########################
class ProductoListApiView(ListAPIView):
    serializer_class = ProductoSerializer
    def get_queryset(self):
        return Producto.objects.all()

class ProductoDetailView(RetrieveAPIView):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.filter()

class ProductoCreateView(CreateAPIView):
    serializer_class = ProductoCreateSeralizer

class ProductoDeleteView(DestroyAPIView):
    serializer_class = ProductoCreateSeralizer
    queryset = Producto.objects.all()

class ProductoUpdateView(UpdateAPIView):
    serializer_class = ProductoCreateSeralizer
    queryset = Producto.objects.all()

#################       tipo de movimiento    #######################
class TipoMovimientoListApiView(ListAPIView):
    serializer_class = TipoMovimientoSerializer
    def get_queryset(self):
        return TipoMovimiento.objects.all()

#################       Stock    #######################
class StockListApiView(ListAPIView):
    serializer_class = ProductoMovimientoSerializer
    def get_queryset(self):
        return Producto.objects.all()

class StockLoteListApiView(ListAPIView):
    serializer_class = ProductoBatchSerializer
    def get_queryset(self):
        return ProductoBatch.objects.all()
#################       movimiento stock    #######################
class MovimientoStockListApiView(ListAPIView):
    serializer_class = MovimientoSerializer
    def get_queryset(self):
        return MovimientoStock.objects.all()

class MovimientoStockAlmacenListApiView(ListAPIView):
    serializer_class = MovimientoSerializer
    def get_queryset(self):
        kword = self.kwargs['kword']
        return MovimientoStock.objects.filter(
            almacen = kword
        )

class MovimientoStockProductoListApiView(ListAPIView):
    serializer_class = MovimientoSerializer
    def get_queryset(self):
        kword = self.kwargs['kword']
        return MovimientoStock.objects.filter(
            producto = kword
        )

class MovimientoStockCreateView(CreateAPIView):
    queryset = MovimientoStock.objects.all()
    serializer_class = MovimientoStockCreateSerializer

    # def perform_create(self, serializer):
    #     movimiento = serializer.save()
        # productostock = ProductoStock(
        #     producto = serializer.validated_data['producto'],
        #     almacen = serializer.validated_data['almacen'],
        #     valor = serializer.validated_data['valor'],
        # )


    # def perform_create(self, serializer):
    #     movimiento = serializer.save()
    #     ProductoStock.objects.create(
    #         producto = serializer.validated_data['producto'],
    #         almacen = serializer.validated_data['almacen'],
    #         valor = serializer.validated_data['valor'],
    #     )
        

class MovimientoStockLoteCreateView(CreateAPIView):
    serializer_class = MovimientoStockLoteCreateSerializer

##############      CATEGORIA VIEWS      #########################
class CategoriaListApiView(ListAPIView):
    serializer_class = CategoriaSerializer
    def get_queryset(self):
        return Categoria.objects.all()

class CategoriaCreateView(CreateAPIView):
    serializer_class = CategoriaCreateSerializer

class CategoriaDetailView(RetrieveAPIView):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.filter()

class CategoriaDeleteView(DestroyAPIView):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()

class CategoriaUpdateView(UpdateAPIView):
    serializer_class = CategoriaCreateSerializer
    queryset = Categoria.objects.all()

##############      GRUPO VIEWS      #########################
class GrupoListApiView(ListAPIView):
    serializer_class = GrupoSerializer
    def get_queryset(self):
        return Grupo.objects.all()

class GrupoCreateView(CreateAPIView):
    serializer_class = GrupoCreateSerializer

class GrupoDetailView(RetrieveAPIView):
    serializer_class = GrupoSerializer
    queryset = Grupo.objects.filter()

class GrupoDeleteView(DestroyAPIView):
    serializer_class = GrupoSerializer
    queryset = Grupo.objects.all()

class GrupoUpdateView(UpdateAPIView):
    serializer_class = GrupoCreateSerializer
    queryset = Grupo.objects.all()

##############      PROVEEDOR VIEWS      #########################
class ProveedorListApiView(ListAPIView):
    serializer_class = ProveedorSerializer
    def get_queryset(self):
        return Proveedor.objects.all()

class ProveedorCreateView(CreateAPIView):
    serializer_class = ProveedorCreateSerializer

class ProveedorDetailView(RetrieveAPIView):
    serializer_class = ProveedorSerializer
    queryset = Proveedor.objects.filter()

class ProveedorDeleteView(DestroyAPIView):
    serializer_class = ProveedorSerializer
    queryset = Proveedor.objects.all()

class ProveedorUpdateView(UpdateAPIView):
    serializer_class = ProveedorCreateSerializer
    queryset = Proveedor.objects.all()