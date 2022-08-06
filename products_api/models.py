from django.db import models


class Products(models.Model):
    imgName  = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=100000, default="100.20")

    
    def __str__(self):
        return "{} - {()}".format(self.imgName, self.title)
    
