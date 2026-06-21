from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home'),
    path('', views.hotel_list, name='hotel_list'),
    path('search/', views.hotel_list, name='search_hotels'),
    
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico')), name='favicon'),
    path('.well-known/appspecific/com.chrome.devtools.json', lambda r: HttpResponse(status=200)),
    path('profile/', views.profile_page, name='profile'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_view, name='register'),
    path('about/', views.about_page, name='about'),
    path('help/', views.help_page, name='help'),
    path('careers/', views.careers_page, name='careers'),
    path('feedback/', views.feedback_page, name='feedback'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)