from django.urls import path
from .views import Login, Logout, Signup, home, dashboard, create, detail, search, book_event, update, profile

urlpatterns = [
	path('', home, name='home'),
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/<str:user_name>/', profile, name='profile'),

    path('create/', create, name='create'),
    path('detail/<int:event_id>/', detail, name='detail'),
    path('search/', search, name='search'),
    path('book/<int:event_id>/', book_event, name='book'),
    path('update/<int:event_id>/', update, name='update'),





    
]