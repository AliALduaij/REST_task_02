from rest_framework.generics import ListAPIView , RetrieveAPIView , RetrieveUpdateAPIView , DestroyAPIView
from datetime import datetime

from .models import Flight, Booking
from .serializers import FlightSerializer, BookingSerializer ,BookingRSerializer , BookingUSerializer


class FlightsList(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer


class BookingsList(ListAPIView):
	queryset = Booking.objects.filter(date__gte=datetime.today())
	serializer_class = BookingSerializer

class BookingRetrieve(RetrieveAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookingRSerializer
	lookup_field= 'id'
	lookup_url_kwarg= 'azeeza'


class BookingUpdate(RetrieveUpdateAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookingUSerializer
	lookup_field= 'id'
	lookup_url_kwarg= 'ali'

class BookingDelete(DestroyAPIView):
	queryset = Booking.objects.all()
	lookup_field= 'id'
	lookup_url_kwarg= 'maryam'
