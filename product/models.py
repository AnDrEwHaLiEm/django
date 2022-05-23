from django.db import models


class Category(models.Model):
    categoryName = models.CharField(max_length=15)

    def __str__(self):
        return self.categoryName


class Product(models.Model):
    productName = models.CharField(max_length=12)
    proudctDescription = models.CharField(max_length=600)
    productBrand = models.CharField(max_length=12)
    productPrice = models.PositiveBigIntegerField()
    productColor = models.CharField(max_length=100)
    productSize = models.CharField(max_length=100)
    productImage = models.ImageField()
    productType = models.ForeignKey(Category, on_delete=models.CASCADE)


class Cart(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def _str_(self):
        return self.product.productName