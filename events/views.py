from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import UserSignup, UserLogin, BookForm, EventForm, UserProfileForm
from django.contrib import messages
from .models import Event, Book, UserProfile, Relationship
from datetime import datetime
from datetime import date
from datetime import time
from django.utils import timezone

from django.db.models import Q
from django.contrib.auth.models import User


def home(request):
    if request.user.is_anonymous :
        return redirect ("login")
       
    context = {
        'event' : Event.objects.filter(date__gte=datetime.now()),
    }
    return render(request, 'home.html', context)


def dashboard(request):
    if request.user.is_anonymous :
        return redirect ("login")

    # history_obj = Book.objects.filter(user=request.user)
    history_obj = Book.objects.filter(user=request.user, event__date__lt =datetime.now())
    my_bookings = Book.objects.filter(user=request.user, event__date__gte =datetime.now())
    events = Event.objects.filter(owner=request.user)

    context = {
        'event' : events,   # naming
        'history' : history_obj,
        'my_bookings': my_bookings,
    }
    return render(request, 'dashboard.html', context)


def cancel_upcoming_booking(request, booking_id ):
    if request.user.is_anonymous :
        return redirect ("login")

    booking_obj = Book.objects.get(id=booking_id)

    if not booking_obj.user == request.user:
        return redirect('no-access')
    
    date_time_compbination = datetime.combine(booking_obj.event.date, booking_obj.event.time)
    difference = date_time_compbination - datetime.today()
    
    days, seconds = difference.days, difference.seconds 
    hours = days * 24 + seconds // 3600

    if datetime.today() <= date_time_compbination and hours > 3:
        booking_obj.delete()
    else:
        return redirect('dashboard')
    return redirect('dashboard')





def profile(request, user_name):
    if request.user.is_anonymous :
        return redirect ("login")
    user=User.objects.get(username=user_name)
    event=Event.objects.filter(owner=request.user)
    context = {
        'user' : UserProfile.objects.get(user=user),
        'event' : event,
    }

    return render(request, 'profile.html', context)

def edit_profile(request, user_name) :
    user = User.objects.get(username=user_name)
    user_obj = UserProfile.objects.get(user=user)
    form = UserProfileForm(instance=user_obj)
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=user_obj)
        if form.is_valid():
            form.save()
            return redirect('profile', user_name)
    context = {
        "form": form,
        "user": user_obj,
        }
    return render(request, 'editprofile.html', context)


def find_user(request):
    user = UserProfile.objects.all()
    query = request.GET.get('q')
    
    if query:
        user = user.filter(
            Q(user__username__icontains=query)|  
            Q(first_name__icontains=query)|
            Q(last_name__icontains=query)|
            Q(country__icontains=query)|
            Q(bio__icontains=query)
             ).distinct()

    context = {
        'user' : user,
    }

    return render(request, 'finduser.html', context)



def search(request):
    event = Event.objects.filter(date__gte=datetime.now())

    query = request.GET.get('q')
    # As a user I can search for an event either 
    # by it's title, description or organizer.
    if query:
        event = event.filter(
            # we need to get the username from the owner field
            Q(owner__username__icontains=query)|  
            Q(title__icontains=query)|
            Q(description__icontains=query)

             ).distinct()


    context = {
        'event' : event,
    }

    return render(request, 'search.html', context)



def book_event(request,event_id):
    if request.user.is_anonymous:
        return redirect ('login')

    event_obj = Event.objects.get(id=event_id)
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)

        tickets = request.POST.get('tickets', None)

        if event_obj.get_available_tickets() <= int(tickets):
            messages.warning(request, "you can't book, There are no enough available tickets! ")

        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.event = event_obj
            book.save()  

            return redirect('home')

    context = {
    'event': event_obj,
     'form': form, 


    }
    return render(request, 'book.html', context)
    

def create(request):
    if request.user.is_anonymous :
        return redirect ('login')
    form = EventForm()
    if request.method == "POST" :
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)

            event.owner = request.user

            event.save()
            return redirect ('dashboard')
    context = {
        'form' : form,
    }
    return render (request, 'create.html', context)



def update(request, event_id) :
   event = Event.objects.get(id=event_id)
   form = EventForm(instance=event)
   if request.method == "POST":
       form = EventForm(request.POST, request.FILES, instance=event)
       if form.is_valid():
           form.save()
           return redirect('detail', event_id)
   context = {
       "form": form,
       "event": event,
   }
   return render(request, 'update.html', context)




class Signup(View):
    form_class = UserSignup
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            messages.success(request, "You have successfully signed up.")
            login(request, user)
            return redirect("home")
            
        messages.warning(request, form.errors)
        return redirect("signup")


class Login(View):
    form_class = UserLogin
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                messages.success(request, "Welcome Back!")
                return redirect('home')
            messages.warning(request, "Wrong email/password combination. Please try again.")
            return redirect("login")
        messages.warning(request, form.errors)
        return redirect("login")


class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, "You have successfully logged out.")
        return redirect("login")



def detail (request, event_id) :
    event = Event.objects.get(id=event_id)
    booking_obj = Book.objects.filter(event__owner= request.user, event= event_id  ).distinct()

    # booking_obj = Book.objects.filter(user=request.user)



    context = {
    'event': event,
    'booking_obj': booking_obj,

    }
    return render(request, 'detail.html', context)



def no_access(request):
    return render(request, 'no_access.html')

    