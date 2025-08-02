from rest_framework import viewsets
from .models import Listing, Booking
from .serializer import ListingSerializer, BookingSerializer

class ListingViewSet(viewsets.ModelViewSet):
    """
    Provides a CRUD endpoint for Listing models:
    list, retrieve, create, update, and partial_update, distory.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    """
    Provides a CRUD endpoints for Booking models:
    list, retrieve, create, update, and partial_update, distory.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_queryset(self):
        """
        provides CRUD endpoints for Booking model.
        """
        queryset = Booking.objects.all()
        serializer_class = BookingSerializer