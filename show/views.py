from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import Contactform, BookingForm
from .models import Instrument,Concert,Book,Team,Article,Album,Testmonial,Seat
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.models import User
def index(request):
    concert=Concert.objects.all()
    context={
        "concert":concert,
    }
    return render (request,"index.html",context)
def about(request):
    data=Instrument.objects.all()
    mem=Team.objects.all()
    context={
        "data":data,
        "mem":mem
    }
    return render (request,"about.html",context)
def registration(request):
    form=UserCreationForm() 
    if request.method =='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            form=UserCreationForm() 
            return redirect("/")
        return redirect("/") 
    return render(request,"registration.html",{"form":form})
@login_required 
def book(request):
    concert=Concert.objects.all()
    if request.method=="POST":
        name=request.POST['name']
        address=request.POST['address']
        email=request.POST['email']
        phone=request.POST['phone']
        venue=request.POST['venue']
        date=request.POST['date']
        time=request.POST['time']
        print(name)
        form=Book(name=name,address=address,email=email,phone=phone,venue=venue,date=date,time=time)
        form.save()  
        return redirect("seat")
    return render (request,"book.html", {"concert":concert})
def seat(request):
    book=Book.objects.all()
    seats = Seat.objects.filter(is_available=True)
    return render(request,"seat.html",{"seats": seats})
def book_seat(request, seat_id):
    name=request.user
    data=Book.objects.filter(name=name)[0]
    seat = Seat.objects.get(id=seat_id)
    if not seat.is_available:
        messages.error(request, "This seat is already booked.")
        return redirect('seat_list')
        if form.is_valid():
                booking = form.save(commit=False)
                booking.user = request.user
                booking.seat = seat
                booking.save()
                seat.is_available = False  # Mark seat as booked
                seat.save()
                messages.success(request, f"You have successfully booked {seat}.")
                return redirect("book")
    else:
            form = BookingForm()
    return render(request, 'book_seat.html', {'form': form, 'seat': seat,'data':data})

def contact(request):
    testmonial=Testmonial.objects.all()
    form=Contactform()
    if request.method=='POST':
        form=Contactform(request.POST)
        if form.is_valid():
            form.save()
            form=Contactform()
            return redirect("contact")
    context={
        "form":form,
        "testmonial":testmonial
    }
    return render(request,"contact.html",context)
def article(request):
    album=Album.objects.all()
    news=Article.objects.all()
    context={
        "album":album,
        "news":news
    }
    return render (request,"article.html",context)
def logout(request):
    logout(request)
    return redirect("/")


