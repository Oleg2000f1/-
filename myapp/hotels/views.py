from django.shortcuts import render
from .models import Hotel

def home_page(request):
    return render(request, 'hotels/index.html')

def hotel_list(request):
    hotels = Hotel.objects.all()
    
    city = request.GET.get('city', '').strip()
    max_price = request.GET.get('max_price', '').strip()
    stars = request.GET.get('stars', '').strip()

    if city:
        hotels = hotels.filter(city__icontains=city)
    if max_price:
        hotels = hotels.filter(price_per_night__lte=max_price)
    if stars:
        hotels = hotels.filter(stars=stars)

    context = {
        'hotels': hotels,
        'city': city,
        'max_price': max_price,
        'stars': stars
    }
    return render(request, 'hotels/hotel_list.html', context)

def hotel_list(request):
    return render(request, 'hotels/hotel_list.html')
