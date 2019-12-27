from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Setting(models.Model):
    # This is Model
    site_name = models.CharField(max_length=64, blank=True)
    mobile = models.CharField(max_length=15, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=64, blank=True)
    address1 = models.CharField(max_length=64, blank=True)
    address2 = models.CharField(max_length=64, blank=True)
    country = models.CharField(max_length=64, blank=True)
    city = models.CharField(max_length=64, blank=True)
    state = models.CharField(max_length=64, blank=True)
    # start_date = models.TimeField(auto_now=False, auto_now_add=False,blank=True)
    # end_date = models.TimeField(auto_now=False, auto_now_add=False,blank=True)
    zip_code = models.CharField(max_length=64, blank=True)
    about_us = models.CharField(max_length=500, blank=True)
    tw_url = models.CharField(max_length=200, blank=True)
    fb_url = models.CharField(max_length=200, blank=True)
    inst_url = models.CharField(max_length=200, blank=True)
    pin_url = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return ("{} {} {} {}".format(self.hotal, self.phone, self.email, self.address1))

class Categorie(models.Model):
    name = models.CharField(max_length=64, blank=True)
    create_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return ("{}".format(self.name))

class Tag(models.Model):
    name = models.CharField(max_length=64, blank=True)
    create_at = models.DateTimeField(auto_now=True, blank=True)
    class Meta:
        ordering = ['name']
    def __str__(self):
        return ("{}".format(self.name))

class product(models.Model):
    """docstring for product."""
    name = models.CharField(max_length=64, blank=True)
    categ_id = models.ForeignKey(Categorie, blank=True, on_delete=models.CASCADE, related_name="categ_item")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    create_at = models.DateTimeField(auto_now=True, blank=True)
    image = models.ImageField(upload_to="images/product", default="imd-3.jpg")
    desic = models.TextField(max_length=100, blank=True)
    tags = models.ManyToManyField(Tag)
    # class Meta:
    #     ordering = ['name']

    def __str__(self):
        return ("{} {} {} {}".format(self.name, self.categ_id, self.price, self.tags))

class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_name",default=1)
    ordered = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    shopping = models.FloatField(default=0)
    subtotal = models.FloatField(default=0)
    total = models.FloatField(default=0)

    def __str__(self):
        return ("{} {}".format(self.customer, self.total))

class Oreder(models.Model):
    product_id = models.ForeignKey(product, blank=True,  on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Cart, blank=True,  on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    subtotal = models.FloatField(default=0)
    create_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return ("{} {} {}".format(self.product_id, self.cart_id, self.subtotal))
