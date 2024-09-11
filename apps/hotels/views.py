from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Hotel
from .serializers import GetHotelHomePageSerializer

class GetHotelHomePage(APIView):
  def get(self, request, hotel_name):
    hotel = get_object_or_404(Hotel, hotel_name=hotel_name)
    serializer = GetHotelHomePageSerializer(hotel)
    return Response(serializer.data)