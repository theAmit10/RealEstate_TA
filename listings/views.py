from django.shortcuts import render,get_object_or_404
from .models import Listing
from .choices import state_choices,price_choices,bedroom_choices

# Create your views here.
def index(request):
    listings = Listing.objects.all()

    context = {
        'listings' : listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
	listing = get_object_or_404(Listing, pk=listing_id)
	
	context = {
		'listing': listing
	}
	return render(request, 'listings/listing.html', context) 


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # getting keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords) # description__icontains= this will check the simialr type of word in the databse which is similar to keywords. in which __icontains is used to find the similar type of words.

    # searchiing through city name 
    if 'city' in request.GET:
        city = request.GET['city'] # in server this is checking name which have 'city' as its name. its checking name attribute in the server site.
        if city:
            queryset_list = queryset_list.filter(city__iexact=city) # here iexact means i = because of i it becomse not case sensitive 
    
    # searchiing through state name 
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # searchiing through bedrooms name 
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)# lte = less than or equal to

    # searchiing through price name 
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'state_choices': state_choices, # this used 
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values' : request.GET # this is used to hold the values in the search field .
    } 

    return render(request, 'listings/search.html', context)
