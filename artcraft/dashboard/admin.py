from django.contrib import admin
from .models import Artist, Customer, Artwork, Order

admin.site.register(Artist)
admin.site.register(Customer)
admin.site.register(Artwork)
admin.site.register(Order)
# Register your models here.
