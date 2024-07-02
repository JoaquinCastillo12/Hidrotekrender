from django.db import models 
from django.contrib.auth.models import User
from django.db.models import Sum

class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    id = models.AutoField(primary_key=True) 
    name= models.CharField(max_length=100)
    price= models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description= models.CharField(max_length=250, default='', blank=True, null=True)
    image= models.ImageField(upload_to='uploads/product/')

    def __str__(self):
        return self.name 
    

    def __str__(self):
        return self.product
    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField('Product', through='CartItem')

    def __str__(self):
        return f"Cart for {self.user.username}"

    @property
    def total_items(self):
        total_items = 0
        cart_items = CartItem.objects.filter(cart=self)
        for item in cart_items:
            total_items += item.quantity
        return total_items
    @property
    def total(self):
        total = 0
        cart_items = self.cartitem_set.all()
        for item in cart_items:
            total += item.quantity * item.product.price
        return total
    def update_total(self):
        total = sum(item.quantity * item.product.price for item in self.cartitem_set.all())
        self.total = total
        self.save()

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)     
    def __str__(self):
        return f"{self.quantity} of {self.product.name} in cart {self.cart.id}"
    def save(self, *args, **kwargs):
        self.subtotal = self.quantity * self.product.price
        super().save(*args, **kwargs)
