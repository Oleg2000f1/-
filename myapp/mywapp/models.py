from django.db import models
from django.contrib.auth.models import User

class Hotel(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название отеля")
    city = models.CharField(max_length=100, default="Москва", verbose_name="Город")
    price_per_night = models.IntegerField(default=3000, verbose_name="Цена за ночь (руб.)")
    stars = models.IntegerField(default=3, verbose_name="Количество звезд")
    description = models.TextField(blank=True, default="", verbose_name="Описание отеля")
    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_bookings')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='bookings', null=True)
    checkin = models.DateField(verbose_name="Дата заезда")
    checkout = models.DateField(verbose_name="Дата выезда")
    guest_name = models.CharField(max_length=100, verbose_name="Имя гостя")
    guest_phone = models.CharField(max_length=20, verbose_name="Телефон")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата оформления")

class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name="Электронная почта")
    subject = models.CharField(max_length=200, verbose_name="Тема сообщения")
    message = models.TextField(verbose_name="Текст сообщения")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")

    # Внутри класса Meta ОБЯЗАТЕЛЬНО должны быть отступы (4 пробела)
    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"

    # Внутри метода __str__ ОБЯЗАТЕЛЬНО должны быть отступы (4 пробела)
    def __str__(self):
        return f"Сообщение от {self.name} — {self.subject}"

    # НОВОЕ ПОЛЕ: варианты категорий жилья
    TYPE_CHOICES = [
        ('hotel', 'Отель'),
        ('apartment', 'Квартира'),
        ('house', 'Дом и коттедж'),
        ('hostel', 'Хостел'),
    ]
    property_type = models.CharField(
        max_length=20, 
        choices=TYPE_CHOICES, 
        default='hotel', 
        verbose_name="Тип жилья"
    )

    # НОВЫЕ ПОЛЯ: Даты, когда отель уже КЕМ-ТО ЗАНЯТ
    booked_from = models.DateField(null=True, blank=True, verbose_name="Занят с")
    booked_to = models.DateField(null=True, blank=True, verbose_name="Занят по")

    # НОВЫЕ ПОЛЯ ДЛЯ СОВРЕМЕННОГО ПОИСКА
    has_wifi = models.BooleanField(default=True, verbose_name="Бесплатный Wi-Fi")
    has_pool = models.BooleanField(default=False, verbose_name="Бассейн")
    has_breakfast = models.BooleanField(default=False, verbose_name="Завтрак включен")

    def __str__(self):
        return f"{self.name} ({self.city})"