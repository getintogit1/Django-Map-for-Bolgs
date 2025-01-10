# pages/urls.py

from django.urls    import path
from pages          import views

urlpatterns = [
    path('', views.home_screen_view, name = 'home'),
    path('kontakt', views.kontakt_page_view, name = 'kontakt'),
    path('kontakt', views.impressum_page_view, name = 'impressum'),
    path('kontakt', views.datenschutz_page_view, name = 'datenschutz'),
]