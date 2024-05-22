from django.db import models

from django.shortcuts import render


# Create your models here.


class userLogin(models.Model):
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=50)
    username = models.TextField()
    phone_num = models.IntegerField()

class Celeb(models.Model):
    #login_id = models.ForeignKey(userLogin, on_delete=models.CASCADE)
    MUSIC = 'Music'
    ACTOR = 'Actor/Actress'
    COMEDY = 'Comedy'
    STANDUP_ARTIST = 'Standup Artist'
    CATEGORY_CHOICES = [(MUSIC, 'Music'),(ACTOR, 'Actor/Actress'),(COMEDY, 'Comedy'),(STANDUP_ARTIST, 'Standup Artist')]
    NIGERIA = 'Nigeria'
    USA = 'USA'
    SOUTH_AFRICA = 'South Africa'
    CANADA = 'Canada'
    AUSTRALIA = 'Australia'
    COUNTRY_CHOICES = [(NIGERIA, 'Nigeria'),(USA, 'USA'),(SOUTH_AFRICA, 'South Africa'),(CANADA, 'Canada'),(AUSTRALIA, 'Australia')]

    stage_name = models.CharField(max_length=100)
    entertainment_category = models.CharField(max_length=20,choices=CATEGORY_CHOICES,default=MUSIC)
    date_of_birth = models.DateField()
    country = models.CharField(max_length=20,choices=COUNTRY_CHOICES, default=NIGERIA)
    face_book_name = models.TextField()
    X_handle = models.TextField()
    Insta_handle = models.TextField()
    verification_status= models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #Terms_agreement = models.BooleanField(defualt = False)
    
    def __str__(self):
        return self.stage_name
    
class ngo(models.Model):
        #login_id = models.ForeignKey(userLogin, on_delete=models.CASCADE)
        NGO_name = models.CharField(max_length=100)
        Registration_number = models.IntegerField()
        Year_of_registration = models.IntegerField()
        website = models.CharField(max_length=100)
        NGO_type = models.TextField()
        office_address = models.CharField(max_length=100)
        Country = models.CharField(max_length=50)
        State = models.CharField(max_length=100)
        Terms = models.BooleanField(default=False)
        
        def __str__(self):
            return self.NGO_name
        
class Fans(models.Model):
    #login_id = models.ForeignKey(userLogin,on_delete=models.CASCADE)
    Legal_name = models.CharField(max_length=100,default='')
    country = models.CharField(max_length=20,default='')
    terms = models.BooleanField(default=False)
    DAVIDO = 'davido'
    AY = 'ay'
    SEYI_LAW = 'seyi_law'
    ACTOR_CHOICES = [(DAVIDO , 'davido'),(AY , 'ay'),(SEYI_LAW , 'seyi_law')]    
    Fan_of = models.CharField(max_length=100,choices=ACTOR_CHOICES,default=AY )
    
    def __str__(self):
        return self.Legal_name



