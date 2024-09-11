from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.reservations.serializers import ReservationCreateSerializer

class ReserveUsers(APIView):
  def post(self, request):
    serializer = ReservationCreateSerializer(data=request.data, context={'request': request})
        
    if serializer.is_valid():
      reservation = serializer.save()
      return Response({"message": "Reservation created successfully", "reservation_id": reservation.id}, status=status.HTTP_201_CREATED)
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
