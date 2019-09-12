from django.contrib import admin
from .models import Event, Book, Relationship, UserProfile


admin.site.register(Event)
admin.site.register(Book)
admin.site.register(Relationship)
admin.site.register(UserProfile)
