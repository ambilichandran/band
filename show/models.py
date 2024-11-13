from django.db import models
from django.contrib.auth.models import User
class Instrument(models.Model):
    name=models.CharField(max_length=100,blank=None)
    image=models.ImageField(upload_to="image")
    description=models.TextField(max_length=300,blank=True)
    def __str__(self):
        return self.name
class Concert(models.Model):
        image=models.ImageField(upload_to="image",blank=True)
        band=models.CharField(max_length=100,blank=True)
        venue=models.CharField(max_length=100,blank=None)
        date=models.DateField()
        time=models.TimeField()
        def __str__(self):
            return self.band
class Book(models.Model):
    name=models.CharField(max_length=50,blank=True)
    address=models.TextField(max_length=100,blank=None)
    email=models.EmailField()
    phone=models.IntegerField()
    venue=models.TextField(null=True)
    date=models.TextField(null=True)
    time=models.TextField(null=True)
    def __str__(self):
        return self.name 
class Team(models.Model):
    name=models.CharField(max_length=50,blank=None)
    equip=models.ForeignKey(Instrument,on_delete=models.CASCADE)
    img=models.ImageField(upload_to="image")
    about=models.CharField(max_length=200,blank=None)
    def __str__(self):
        return self.name  
class Article(models.Model):
    date=models.DateField()
    image=models.ImageField(upload_to="image",blank=True)
    heading=models.CharField(max_length=100,blank=None) 
    main=models.TextField(max_length=200,blank=None) 
def __str__(self):
        return self.heading
class Album(models.Model):
    sl=models.CharField(max_length=5,blank=True)
    image=models.ImageField(upload_to="image",blank=None)
def __str__(self):
        return self.sl   
class Contact(models.Model):
    name=models.CharField(max_length=100,blank=None)
    email=models.EmailField()
    phone=models.IntegerField()
    message=models.TextField(max_length=200,blank=None)
def __str__(self):
        return self.name    
class Testmonial(models.Model):
    image=models.ImageField(upload_to="image",blank=True)
    name=models.CharField(max_length=100,blank=None)
    profession=models.CharField(max_length=80,blank=None)
    message=models.TextField(max_length=150,blank=None)
def __str__(self):
        return self.name 

class Seat(models.Model):
    number = models.CharField(max_length=10, unique=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Seat {self.number}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Booking by {self.user} for {self.seat}"         

        
