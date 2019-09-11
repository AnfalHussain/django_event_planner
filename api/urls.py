from django.urls import path
from api.views import (ListBookedEventsView, CreateEventView,
    UpdateEventView, ListWhoBookedMyEventsView, BookEventView,
    FollowView, UnfollowView, ListWhoAmIFollowingView, 
    ListView, SpecificView, SignupView, LoginView )

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('ListBookedEvents/', ListBookedEventsView.as_view(), name='ListBookedEvents'),
    path('CreateEvent/', CreateEventView.as_view(), name='CreateEvent'),
    path('UpdateEvent/<int:event_id>/', UpdateEventView.as_view(), name='UpdateEvent'),
    path('WhoBookedMyEvents/', ListWhoBookedMyEventsView.as_view(), name='BookedMyEvents'),
    path('BookEvent/<int:event_id>/', BookEventView.as_view(), name='BookEvent'),
    path('Follow/', FollowView.as_view(), name='Follow'),
    path('unfollow/<str:following_username>/', UnfollowView.as_view(), name='unfollow'),
    path('MyFollowing/', ListWhoAmIFollowingView.as_view(), name='BookedMyEvents'),


    path('APIlist/', ListView.as_view(), name='APIlist'),
    path('APISpecificOrganizer/<str:username>/', SpecificView.as_view(), name='APISpecific'),
    path('APIsignup/', SignupView.as_view(), name="APIsignup"),
    path('APIlogin/', LoginView.as_view(), name="APIlogin"),


    path('loginAPI/', TokenObtainPairView.as_view(), name="loginAPI"),



]