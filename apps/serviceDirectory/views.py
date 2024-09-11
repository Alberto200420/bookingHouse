from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from django.shortcuts import get_object_or_404
from .models import Service, Category
from .serializers import ServiceSerializer, TodayServiceSerializer, CategorySerializer

class GetTodayServices(APIView):
  def get(self, request):
    today = datetime.now().strftime('%A')  # Get current day of the week (e.g., "Monday")
    services_today = Service.objects.filter(availabilities__has_key=today)
    serializer = TodayServiceSerializer(services_today, many=True, context={'today': today})
    return Response(serializer.data)

class GetCategory_and_ServiceList(APIView):
  def get(self, request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

class GetService(APIView):
  def get(self, request, service_id):
    service = get_object_or_404(Service, id=service_id)
    serializer = ServiceSerializer(service)
    return Response(serializer.data)
