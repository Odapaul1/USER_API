from rest_framework import serializers
from .models import Celeb,userLogin,ngo,Fans



class userLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = userLogin
        fields = '__all__'


class CelebSerializer(serializers.ModelSerializer):
    class Meta:
        model = Celeb
        fields = '__all__' 
        
        
class ngoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ngo
        fields = '__all__'

class FansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fans
        fields = '__all__'