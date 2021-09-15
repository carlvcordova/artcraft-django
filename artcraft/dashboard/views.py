from django.shortcuts import render
from django.views.generic import View
from .forms import *
# Create your views here.


class dashboardView(View):
    def get(self, request):
        
        artist = Artist.objects.all()
        customer = Customer.objects.all()
        artwork = Artwork.objects.all()
        order = Order.objects.all()
        return render(request, 'dashboard.html', {'artist':artist, 'customer':customer, 'artwork':artwork, 'order':order})

