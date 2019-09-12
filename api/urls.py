from django.urls import path
from api.views import (ListBookedEventsView, CreateEventView,
    UpdateEventView, ListWhoBookedAnEventView, BookEventView,
    FollowView, UnfollowView, ListWhoAmIFollowingView, 
    ListView, SpecificView, SignupView, LoginView )

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('list/bookedEvents/', ListBookedEventsView.as_view(), name='ListBookedEvents'),
    path('create/event/', CreateEventView.as_view(), name='CreateEvent'),
    path('update/event/<int:event_id>/', UpdateEventView.as_view(), name='UpdateEvent'),
    path('who/booked/event/<int:event_id>/', ListWhoBookedAnEventView.as_view(), name='BookedMyEvents'),
    path('book/event/<int:event_id>/', BookEventView.as_view(), name='BookEvent'),
    path('follow/', FollowView.as_view(), name='Follow'),
    path('unfollow/<str:following_username>/', UnfollowView.as_view(), name='unfollow'),
    path('myFollowing/', ListWhoAmIFollowingView.as_view(), name='BookedMyEvents'),


    path('api/list/', ListView.as_view(), name='APIlist'),
    path('api/specific/organizer/<str:username>/', SpecificView.as_view(), name='APISpecific'),
    path('api/signup/', SignupView.as_view(), name="APIsignup"),
    path('api/login/', LoginView.as_view(), name="APIlogin"),


    path('loginAPI/', TokenObtainPairView.as_view(), name="loginAPI"),



]