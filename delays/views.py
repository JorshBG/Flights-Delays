from django.shortcuts import render, redirect
from django.urls import reverse
from .middlewares import authenticated
from urllib.parse import quote_plus, urlencode
from authlib.integrations.django_client import OAuth
from django.conf import settings
from pathlib import Path
from django.http import JsonResponse
import pandas as pd
from .models import Airports, Airlines, Flights

oauth = OAuth()

oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)


# Create your views here.
def index(request):
    if request.session.get('user'):
        # return render(request, 'pages/auth/about.html', {
        #     'session': request.session.get('user'),
        #     'tab': 'dashboard'
        # })
        return redirect('ds-symbol-map')
    return render(request, 'pages/guest/landing.html')


@authenticated
def profile(request):
    return render(request, 'pages/auth/profile.html', {
        'session': request.session.get('user')
    })


@authenticated
def about(request):
    return render(request, 'pages/auth/about.html', {
        'tab': 'about',
        'session': request.session.get('user')
    })


@authenticated
def dashboard_symbol_map(request):
    return render(request, 'pages/auth/dashboards/symbol-map.html', {
        'session': request.session.get('user'),
        'tab': 'dashboards'
    })


@authenticated
def dashboard_airlines_delays(request):
    return render(request, 'pages/auth/dashboards/airlines-delays.html', {
        'session': request.session.get('user'),
        'tab': 'dashboards'
    })


@authenticated
def dashboard_averages(request):
    return render(request, 'pages/auth/dashboards/averages.html', {
        'session': request.session.get('user'),
        'tab': 'dashboards'
    })


@authenticated
def dataset_flights(request):
    flights = Flights.objects.all()[:50]
    days = {
        1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'
    }

    for flight in flights:
        for day in days:
            if flight.dayOfTheWeek == day:
                flight.dayOfTheWeek = days[day]

    return render(request, 'pages/auth/datasets/flights.html', {
        'session': request.session.get('user'),
        'tab': 'datasets',
        'flights': flights,
        'days': days,
    })


@authenticated
def dataset_airlines(request):
    return render(request, 'pages/auth/datasets/airlines.html', {
        'session': request.session.get('user'),
        'tab': 'datasets',
        'airlines': Airlines.objects.all()
    })


@authenticated
def dataset_airports(request):
    return render(request, 'pages/auth/datasets/airports.html', {
        'session': request.session.get('user'),
        'tab': 'datasets',
        'airports': Airports.objects.all()
    })


# Authentication routes - Auth0
def login(request):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("callback"))
    )


def callback(request):
    token = oauth.auth0.authorize_access_token(request)
    request.session["user"] = token
    return redirect(request.build_absolute_uri(reverse("index")))


@authenticated
def logout(request):
    request.session.clear()

    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("index")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )
