from django.urls import path
from .views import (Login, Logout, Signup, home, dashboard,
 create, detail, search, book_event, update, profile, no_access,
 cancel_upcoming_booking, edit_profile, find_user)
##############################################################

urlpatterns = [
	path('', home, name='home'),
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/<str:user_name>/', profile, name='profile'),
    path('editprofile/<str:user_name>/', edit_profile, name='edit-profile'),
    path('finduser/', find_user, name='finduser'),

    path('create/', create, name='create'),
    path('detail/<int:event_id>/', detail, name='detail'),
    path('search/', search, name='search'),
    path('book/<int:event_id>/', book_event, name='book'),
    path('update/<int:event_id>/', update, name='update'),
    path('cancel/booking/<int:booking_id>/', cancel_upcoming_booking, name='cancel-booking'),
    path('noaccess/', no_access ,name='no-access'),






    
]