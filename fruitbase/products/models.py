from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=50, verbose_name='Имя')
    weight = models.FloatField(verbose_name='Вес (килограмм)')
    price = models.FloatField(verbose_name='Цена')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return self.name
    
    class Meta():
        ordering = ['date']
