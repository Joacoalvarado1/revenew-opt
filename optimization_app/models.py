from django.db import models
from django.utils import timezone

class OptimizationResult(models.Model):
    fecha = models.DateTimeField(default=timezone.now)
    capacidad_a = models.FloatField()
    capacidad_b = models.FloatField()
    producto_a = models.IntegerField()
    producto_b = models.IntegerField()
    ingreso_total = models.FloatField()

    def __str__(self):
        return f"Resultado del {self.fecha.strftime('%Y-%m-%d %H:%M:%S')}"
