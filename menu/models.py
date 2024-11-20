from django.db import models

# Create your models here.

class foodItem(models.Model):
    food_name = models.CharField(max_length=100)
    food_price = models.DecimalField(max_digits=20, decimal_places=2)
    img_url = models.URLField(default="#")

    def __str__(self):
        return self.food_name