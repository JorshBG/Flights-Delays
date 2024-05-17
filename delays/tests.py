from django.test import TestCase
import pandas as pd
from pathlib import Path
from .models import Airlines, Airports, Flights


# Create your tests here.
class ImportDataTestCase(TestCase):
    def setUp(self):
        csv_airlines = pd.read_csv(Path(__file__).resolve().parent.joinpath('data/Airlines.csv'))
        csv_airports = pd.read_csv(Path(__file__).resolve().parent.joinpath('data/Airports.csv'))
        csv_flights = pd.read_csv(Path(__file__).resolve().parent.joinpath('data/Flights.csv'))
        for index, row in csv_airlines.iterrows():
            airline = Airlines(code=row['code'], name=row['name'], country=row['country'])
            airline.save()
        for index, row in csv_airports.iterrows():
            airport = Airports(
                code=row['code'],
                name=row['name'],
                country=row['country'],
                latitude=row['latitude'],
                longitude=row['longitude']
            )
            airport.save()
        for index, row in csv_flights.iterrows():
            flight = Flights(
                flight=row['Flight'],
                airline=Airlines.objects.get(code=row['Airline']),
                airportFrom=Airports.objects.get(code=row['AirportFrom']),
                airportTo=Airports.objects.get(code=row['AirportTo']),
                dayOfTheWeek=row['DayOfWeek'],
                time=row['Time'],
                length=row['Length'],
                delay=row['Delay']
            )
            flight.save()

    def test_airlines(self):
        airlines = Airlines.objects.all()
        self.assertEqual(airlines.count(), 18)

    def test_airports(self):
        airports = Airports.objects.all()
        self.assertEqual(airports.count(), 293)

    def test_flights(self):
        flights = Flights.objects.all()
        self.assertEqual(flights.count(), 539383)
