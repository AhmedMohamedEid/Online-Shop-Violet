from django.contrib import admin

# Register your models here.

from .models import Setting, Categorie, product, Tag, Cart, Oreder

admin.site.register(Setting)
admin.site.register(Categorie)
admin.site.register(product)
admin.site.register(Tag)
admin.site.register(Cart)
admin.site.register(Oreder)
