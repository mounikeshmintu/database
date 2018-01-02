from django.db import models

# Create your models here.
class ProductManager(models.Manager):
    def featured(self): #Product.objects.featured()
        return self.get_queryset().filter(featured=True)
        return self.title
        # return self.title
class  Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)
    image= models.ImageField(upload_to='products/',null=True,blank=True)
    featured=models.BooleanField(default=False)
    objects=ProductManager()
    def __str__(self):
        return self.title
