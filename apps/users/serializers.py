from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreateSerializer(UserCreateSerializer):
  class Meta(UserCreateSerializer.Meta):
    model = User
    fields = ('id', 'email', 'first_name', 'last_name', 'password', 'hotel_belonging')

  def create(self, validated_data):
    user = User.objects.create_user(**validated_data)
    return user