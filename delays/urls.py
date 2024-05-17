from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('callback', views.callback, name='callback'),
    path('profile', views.profile, name='profile'),
    path('about', views.about, name='about'),
    path('dashboard/symbol_map', views.dashboard_symbol_map, name='ds-symbol-map'),
    path('dashboard/averages', views.dashboard_averages, name='ds-averages'),
    path('dashboard/airlines_delays', views.dashboard_airlines_delays, name='ds-airlines-delays'),
    path('dataset/flights', views.dataset_flights, name='dt-flights'),
    path('dataset/airlines', views.dataset_airlines, name='dt-airlines'),
    path('dataset/airports', views.dataset_airports, name='dt-airports'),
]
