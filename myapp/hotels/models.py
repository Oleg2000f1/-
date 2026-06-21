from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    city = models.CharField(max_length=100, verbose_name="Город")
    stars = models.IntegerField(default=3, verbose_name="Звёзды")
    price_per_night = models.IntegerField(verbose_name="Цена за ночь (руб.)")
    description = models.TextField(blank=True, verbose_name="Описание")
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=4.0, verbose_name="Рейтинг")

    def __str__(self):
        return f"{self.name} ({self.city})"