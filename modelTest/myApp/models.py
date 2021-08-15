from django.db import models

# Create your models here.

class Maker(models.Model):
    name = models.CharField(max_length=10)
    country = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class PModel(models.Model):
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    url = models.URLField(default='http://i.imgur.com/Ous4iGB.png')
    
    def __str__(self):
        return self.name


class Product(models.Model):
    pmodel = models.ForeignKey(PModel, on_delete=models.CASCADE)
    nickName = models.CharField(max_length=15, default="超值的手机")
    description = models.TextField(default="no description")
    year = models.PositiveIntegerField(default=2017)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nickName

class PPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=20, default="photo of the priduct")
    url = models.URLField(default='http://i.imgur.com/Z230eeq.pnt')

    def __str__(self):
        return self.description
