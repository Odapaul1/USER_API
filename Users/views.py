
# Create your views here.


from .serializers import ngoSerializer
from django.shortcuts import render
from rest_framework import generics
from .models import Celeb,ngo,userLogin,Fans
from .models import userLogin
from .serializers import CelebSerializer,userLoginSerializer
from .serializers import FansSerializer

# Create your views here.

class UserListCreate(generics.ListCreateAPIView):
    queryset = userLogin.objects.all()
    serializer_class = userLoginSerializer    
    
class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
        queryset = userLogin.objects.all()
        serializer_class = userLoginSerializer
        lookup_field = 'pk'


class CelebListCreate(generics.ListCreateAPIView):
    queryset = Celeb.objects.all()
    serializer_class = CelebSerializer    
    
class CelebRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
        queryset = Celeb.objects.all()
        serializer_class = CelebSerializer
        lookup_field = 'pk'
        
        
class ngoListCreate(generics.ListCreateAPIView):
    queryset = ngo.objects.all()
    serializer_class = ngoSerializer    
    
class ngoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
        queryset = ngo.objects.all()
        serializer_class = ngoSerializer
        lookup_field = 'pk'

class FansListCreate(generics.ListCreateAPIView):
    queryset = Fans.objects.all()
    serializer_class = FansSerializer    
    
class FansRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
        queryset = Fans.objects.all()
        serializer_class = FansSerializer
        lookup_field = 'pk'