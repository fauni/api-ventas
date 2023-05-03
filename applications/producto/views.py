from django.shortcuts import render

from django.views.generic import ListView

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
    MovimientoStock,
)

# serializers
from .serializers import (
    EstadoSerializer,
    AlmacenSerializer,
    AlmacenCreateSeralizer,
    ProductoCreateSeralizer,
    ProductoSerializer,
    MovimientoStockCreateSerializer,
    MovimientoStockLoteCreateSerializer
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

class ProductoUpdateView(UpdateAPIView):
    serializer_class = ProductoCreateSeralizer
    queryset = Producto.objects.all()

class ProductoDeleteView(DestroyAPIView):
    serializer_class = ProductoCreateSeralizer
    queryset = Producto.objects.all()

#################       movimiento stock    #######################
class MovimientoStockListAiView(ListAPIView):
    serializer_class = MovimientoStockCreateSerializer
    def get_queryset(self):
        return MovimientoStock.objects.all()
    
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