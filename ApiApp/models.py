from django.db import models

# Create your models here.
class ProductModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.id} {self.name}'

