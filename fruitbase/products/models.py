from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=50)
    weight = models.FloatField()
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta():
        ordering = ['date']
