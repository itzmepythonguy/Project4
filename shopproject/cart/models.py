from django.db import models
from shopapp.models import product

# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=250,blank=True)
    date_add = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'
        ordering = ['date_add']

    def __str__(self):
        return '{}'.format(self.cart_id)

class CartItem(models.Model):
    products = models.ForeignKey(product,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    qty = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table='CartItem'

    def subtotal(self):
        return self.products.price * self.qty

    def __str__(self):
        return '{}'.format(self.products)
