from django.db import models

# Create your models here.
class ventas(models.Model):
    auto = models.ForeignKey('autos.autos', on_delete=models.CASCADE)
    cliente = models.ForeignKey('clientes.clientes', on_delete=models.CASCADE)
    empleado = models.ForeignKey('empleados.empleados', on_delete=models.CASCADE)
    sucursal = models.ForeignKey('sucursales.sucursales', on_delete=models.CASCADE)
    fecha_venta = models.DateField()
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2) 