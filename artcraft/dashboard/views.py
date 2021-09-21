from django.shortcuts import render
from django.views.generic import View
from .forms import *
# Create your views here.


class dashboardView(View):
    def get(self, request):
        
        return render(request, 'dashboard.html')

class artistView(View):
    def get(self, request):
        
        artist = Artist.objects.all()
        return render(request, 'artist.html', {'artist':artist})

class artworkView(View):
    def get(self, request):
        
        artwork = Artwork.objects.all()

        return render(request, 'artwork.html', {'artwork':artwork})

class customerView(View):
    def get(self, request):
        
        customer = Customer.objects.all()

        return render(request, 'customer.html', {'customer':customer})

class orderView(View):
    def get(self, request):
        
        order = Order.objects.all()
        return render(request, 'order.html', {'order':order})

class signinView(View):
    def get(self, request):
        
        return render(request, 'signin.html')

class signupView(View):
    def get(self, request):
        
        return render(request, 'signup.html')


class homeView(View):
    def get(self, request):
        
        return render(request, 'home.html')