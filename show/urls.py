from django .urls import path
from .import views 
urlpatterns=[
    path("",views.index,name="index"),
    path("about",views.about,name="about"),
    path("registration",views.registration,name="registration"),
    path("book",views.book,name="book"),
    path("seat",views.seat,name="seat"),
    path("contact",views.contact,name="contact"),
    path("article",views.article,name="article"),
    path('book/<int:seat_id>/', views.book_seat, name='book_seat'),
    path("logout",views.logout,name="logout"),
]