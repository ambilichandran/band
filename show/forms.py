from django import forms
from.models import Contact,Booking,Seat 
from django.forms import TextInput,Textarea
class Contactform(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name','email','phone','message']
        widgets={
            'name':TextInput(
                attrs={
                    "type":"text",
                    "class":"form-control",
                    "placeholder":"Full Name"
                }
            ),
            'email':TextInput(
                attrs={
                    "type":"text",
                    "class":"form-control", 
                    "placeholder":"Email Address"
                }
            ),
            'phone':TextInput(
                attrs={
                    "type":"text",
                    "class":"form-control", 
                    "placeholder":"Contact Number"
                }
            ),
            'message':Textarea(
                attrs={
                    "type":"text",
                    "class":"form-control",
                    "placeholder":"write your message"
                }
            )
        }
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['seat']

    def clean_seat(self):
        seat = self.cleaned_data['seat']
        if not seat.is_available:
            raise forms.ValidationError("This seat is already booked.")
        return seat        