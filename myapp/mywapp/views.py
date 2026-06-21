from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Hotel, Booking, Feedback
from .forms import ExtendedRegisterForm

# 1. Главная страница с правильным фильтром дат
def home_page(request):
    hotels = Hotel.objects.all()

    available_cities = Hotel.objects.values_list('city', flat=True).distinct()
    
    city = request.GET.get('city', '').strip()
    stars = request.GET.get('stars', '').strip()
    checkin = request.GET.get('checkin', '').strip()
    checkout = request.GET.get('checkout', '').strip()
    max_price = request.GET.get('max_price', '').strip()

    if city:
        hotels = hotels.filter(city__icontains=city)
        
    if stars:
        hotels = hotels.filter(stars=stars)

    if max_price and hasattr(Hotel, 'price_per_night'):
        hotels = hotels.filter(price_per_night__lte=max_price)

    if checkin and checkout:
        busy_bookings = Booking.objects.filter(
            checkin__lt=checkout,
            checkout__gt=checkin
        )
        busy_hotels_ids = busy_bookings.values_list('hotel_id', flat=True)
        hotels = hotels.exclude(id__in=busy_hotels_ids)

    search_performed = len(city) > 0

    context = {
        'hotels': hotels,
        'city': city,
        'available_cities': available_cities,
        'checkin': checkin,
        'checkout': checkout,
        'search_performed': search_performed
    }
    return render(request, 'index.html', context)

def register_view(request):
    if request.method == 'POST':
        form = ExtendedRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') # Перенаправление на главную после успешной регистрации
    else:
        form = ExtendedRegisterForm()
        
    return render(request, 'register.html', {'form': form})

@login_required # Декоратор закроет доступ для гостей и перенаправит их на логин
def profile_page(request):
    # Находим все бронирования текущего пользователя
    user_bookings = Booking.objects.filter(user=request.user).order_by('-check_in')
    
    context = {
        'bookings': user_bookings
    }
    return render(request, 'profile.html', context)

def hotel_list(request):
    hotels = Hotel.objects.all()
    
    city = request.GET.get('city', '').strip()
    max_price = request.GET.get('max_price', '').strip()
    property_type = request.GET.get('type', '').strip()
    checkin = request.GET.get('checkin', '').strip()
    checkout = request.GET.get('checkout', '').strip()

    # Новые параметры
    stars = request.GET.get('stars', '').strip()
    adults = request.GET.get('adults', '2')
    children = request.GET.get('children', '0')
    wifi = request.GET.get('wifi')
    pool = request.GET.get('pool')
    breakfast = request.GET.get('breakfast')


    if city:
        hotels = hotels.filter(city__icontains=city)
    if max_price:
        hotels = hotels.filter(price_per_night__lte=max_price)
    if property_type:
        hotels = hotels.filter(property_type=property_type)
    if stars:
        hotels = hotels.filter(stars=stars)

         # Фильтр по удобствам (если галочки поставлены)
    if wifi:
        hotels = hotels.filter(has_wifi=True)
    if pool:
        hotels = hotels.filter(has_pool=True)
    if breakfast:
        hotels = hotels.filter(has_breakfast=True)


         # УМНЫЙ ФИЛЬТР ДАТ: Исключаем отели, которые заняты в этот промежуток
    if checkin and checkout:
        hotels = hotels.exclude(
            Q(booked_from__lte=checkout) & Q(booked_to__ge=checkin)
        )

    context = {
        'hotels': hotels,
        'city': city,
        'max_price': max_price,
        'property_type': property_type,
        'checkin': checkin,
        'checkout': checkout
    }
    
    return render(request, 'hotel_list.html', context)

# 1. Личный кабинет (доступен только авторизованным пользователям)
@login_required(login_url='login')
def profile_page(request):
    # Достаем все бронирования текущего залогиненного пользователя
    user_bookings = Booking.objects.filter(user=request.user).order_set_by('-created_at') if hasattr(Booking.objects, 'order_set_by') else Booking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'profile.html', {'bookings': user_bookings})

# 2. Класс для входа (использует встроенную логику Django)
class CustomLoginView(LoginView):
    template_name = 'login.html'  # Имя файла, который мы создадим
    
    def get_success_url(self):
        return '/'  # Куда перенаправлять после успешного входа (на главную)

# 3. Функция для регистрации нового пользователя
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Создаем пользователя в базе данных
            login(request, user)  # Сразу авторизуем его
            return redirect('/')  # Перенаправляем на главную страницу
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

# 4. Вход на сайт
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# 5. Выход из аккаунта
def logout_user(request):
    logout(request)
    return redirect('home')

def about_page(request):
    return render(request, 'about.html')

def help_page(request):
    return render(request, 'help.html')

def careers_page(request):
    return render(request, 'careers.html')

def feedback_page(request):
    success = False
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and subject and message:
            # Сохраняем в базу данных
            Feedback.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            success = True

    return render(request, 'feedback.html', {'success': success})