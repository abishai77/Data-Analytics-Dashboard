from django.db import models

# Create your models here.
from  django.db import models

class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    order_date = models.DateTimeField()

    def __str__(self):
        return self.name