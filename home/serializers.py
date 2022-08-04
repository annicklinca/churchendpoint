from rest_framework import routers, serializers, viewsets
from .models import * 

# create user

  
          
class CharitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Charity
        fields=('__all__') 

class ChurchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChurchDonation
        fields=('__all__') 