from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver


from model_utils.models import TimeStampedModel
from django.utils import timezone


from datetime import datetime

# Create your models here.

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Estado(TimeStampedModel):
    """ Estados de una Tabla """
    estado = models.CharField(
        'Estado',
        max_length=30
    )
    
    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
    
    def __str__(self):
        return self.estado

class TipoMovimiento(TimeStampedModel):
    """ Estados de una Tabla """
    descripcion = models.CharField(
        'Descripcion',
        max_length=30
    )
    
    class Meta:
        verbose_name = 'Tipo de Movimiento'
        verbose_name_plural = 'Tipos de Movimiento'
    
    def __str__(self):
        return self.descripcion


class Almacen (TimeStampedModel):
    """ Almacen del Producto """
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    lugar = models.CharField(max_length=64)
    direccion = models.CharField(max_length=255)
    estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Almacen'
        verbose_name_plural = 'Almacenes'
    
    def __str__(self):
        return self.nombre
    
class Categoria(TimeStampedModel):
    descripcion = models.CharField(max_length=100)
    estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE
    )
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.descripcion

class Grupo(TimeStampedModel):
    descripcion = models.CharField(max_length=100)
    estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE
    )
    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'
    
    def __str__(self):
        return self.descripcion

class Proveedor(TimeStampedModel):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    nit = models.CharField(max_length=20)
    contacto = models.CharField(max_length=250)
    celular = models.CharField(max_length=8)
    estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE
    )
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
    
    def __str__(self):
        return self.nombre

class Producto(TimeStampedModel):
    UNIT_CHOICES = (
        ('0', 'Kilogramos'),
        ('1', 'Litros'),
        ('2', 'Unidades'),
    )

    codigo = models.CharField(max_length=50)
    codigo_barras = models.CharField(
        max_length=13, 
        default=0
    )
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, null=True, blank=True,on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, null=True, blank=True, on_delete=models.CASCADE)
    unidad = models.CharField(
        'Unidad de Medida',
        max_length=1,
        choices=UNIT_CHOICES,
    )
    imagen_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    usa_inventarios = models.BooleanField(default=True)
    usa_lotes = models.BooleanField(default=False)
    stock = models.BigIntegerField()
    stock_minimo = models.IntegerField()
    precio_compra = models.DecimalField(max_digits=7, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=7, decimal_places=2)
    estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE
    )
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
    def __str__(self):
        return self.nombre

class ProductoLote(TimeStampedModel):
    producto = models.ForeignKey(Producto, null=True, blank=True, on_delete=models.CASCADE)
    lote = models.CharField(max_length=30)
    fecha_vencimiento = models.DateTimeField(null=True, blank=True)
    fecha_limite_venta = models.DateTimeField(null=True, blank=True)
    class Meta:
        verbose_name = 'Producto Lote'
        verbose_name_plural = 'Productos Lotes'
    
    def __str__(self):
        return self.producto.nombre + ' - ' + self.lote

class ProductoStock(TimeStampedModel):
    fecha = models.DateTimeField(editable=False, default=timezone.now)
    producto = models.ForeignKey(Producto, null=True, blank=True, on_delete=models.CASCADE)
    almacen = models.ForeignKey(Almacen, null=True, blank=True, on_delete=models.CASCADE)
    valor = models.BigIntegerField()
    class Meta:
        verbose_name = 'Producto Stock'
        verbose_name_plural = 'Productos Stock'
    
    def __str__(self):
        return self.fecha.strftime("%d/%m/%Y %H:%M:%S") + ' - ' + self.producto.nombre + ' - ' + self.almacen.nombre + ' - ' + str(self.valor)
    
    
class MovimientoStock(TimeStampedModel):
    fecha = models.DateTimeField(editable=False, default=timezone.now)
    producto = models.ForeignKey(Producto, null=True, blank=True, on_delete=models.CASCADE)
    lote = models.CharField(max_length=30,null=True, blank=True)
    almacen = models.ForeignKey(Almacen, null=True, blank=True, on_delete=models.CASCADE)
    valor = models.PositiveBigIntegerField()
    precio = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    descripcion = models.CharField(max_length=100, null=True, blank=True)
    fecha_vencimiento = models.DateTimeField(null=True, blank=True, default=timezone.now)
    fecha_limite_venta = models.DateTimeField(null=True, blank=True, default=timezone.now)
    tipo_movimiento = models.ForeignKey(
        TipoMovimiento,
        on_delete=models.CASCADE
    )
    
    class Meta:
        verbose_name = 'Movimiento Stock'
        verbose_name_plural = 'Movimientos Stock'
    
    def save(self, *args, **kwargs):
        existe = False
        try:
            productostock = ProductoStock.objects.get(producto = self.producto, almacen = self.almacen)
            existe = True
        except ProductoStock.DoesNotExist:
            existe = False
        if(existe):
            if self.tipo_movimiento.id == 1:
                productostock.valor = productostock.valor + self.valor
            else:
                productostock.valor = productostock.valor - self.valor
        else:
            productostock = ProductoStock(
                producto = self.producto,
                almacen = self.almacen,
                valor = self.valor
            )
        productostock.save()
        super(MovimientoStock, self).save(*args, **kwargs)

    def __str__(self):
        return self.fecha.strftime("%d/%m/%Y %H:%M:%S") + ' - ' + self.producto.nombre
    
    
def registra_producto_lote(movimientoStock = MovimientoStock):
    productoLote = ProductoLote(
        producto = movimientoStock.producto,
        lote = movimientoStock.lote,
        fecha_vencimiento = movimientoStock.fecha_vencimiento,
        fecha_limite_venta = movimientoStock.fecha_limite_venta
    )
    productoLote.save()
    # return movimientoStock

def crear_modificar_producto_stock(sender, instance, **kwargs):
    if instance.producto.usa_lotes and instance.tipo_movimiento.id == 1:
        registra_producto_lote(instance)
    

def actualizar_stock_producto(sender, instance, **kwargs):
    # print("Signal para actualizar el stock del producto")
    producto = Producto.objects.get(codigo = instance.producto.codigo)
    if instance.tipo_movimiento.id == 1:
        producto.stock = producto.stock + instance.valor
    else:
        producto.stock = producto.stock - instance.valor

    # print (str(producto.stock) + " ---- " + str(instance.valor))
    producto.save()


post_save.connect(crear_modificar_producto_stock, sender = MovimientoStock)
post_save.connect(actualizar_stock_producto, sender=MovimientoStock)