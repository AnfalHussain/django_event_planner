from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView 

from events.models import Event, Book, Relationship
from api.serializers import (ListBookedEventsSerializer, WhoBookedMyEventsSerializer, BookEventSerializer, FollowSerializer, FollowingAUserSerializer, CreateEventSerializer, SignupSerializer, LoginSerializer)

from rest_framework.permissions import IsAuthenticated 
from api.permissions import IsEventOwner, IsFollower
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from datetime import datetime
from django.contrib.auth.models import User



class ListBookedEventsView(ListAPIView):
	serializer_class = ListBookedEventsSerializer
	permission_classes = [IsAuthenticated]

	def get_queryset(self):
		return Book.objects.filter(user=self.request.user,)



class CreateEventView(CreateAPIView):
	serializer_class = CreateEventSerializer
	permission_classes = [IsAuthenticated]


	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)



class UpdateEventView(RetrieveUpdateAPIView):
	queryset = Event.objects.all()
	serializer_class = CreateEventSerializer	
	lookup_field = 'id'
	lookup_url_kwarg = 'event_id'
	permission_classes = [IsAuthenticated, IsEventOwner]



class ListWhoBookedMyEventsView(ListAPIView):
	serializer_class = WhoBookedMyEventsSerializer
	permission_classes = [IsAuthenticated, IsEventOwner]

	def get_queryset(self):
		return Book.objects.filter(event__owner=self.request.user)


class BookEventView(CreateAPIView):
	queryset = Event.objects.all()
	serializer_class = BookEventSerializer
	permission_classes = [IsAuthenticated]
	lookup_field = 'id'
	lookup_url_kwarg = 'event_id'
	

	def perform_create(self, serializer ):

		valid_data = serializer.validated_data
		print(valid_data)
		print(self.get_object().get_available_tickets())
		if valid_data['tickets'] < self.get_object().get_available_tickets():
			return serializer.save(user=self.request.user, event_id=self.kwargs['event_id'])
		else:
			return "There are no enough tickets to book"


class FollowView(CreateAPIView):
	serializer_class = FollowSerializer
	permission_classes = [IsAuthenticated]


	def perform_create(self, serializer):
		serializer.save(follower=self.request.user)


class UnfollowView(DestroyAPIView):
	queryset = Relationship.objects.all()
	lookup_field = 'following__username'
	lookup_url_kwarg = 'following_username'
	permission_classes = [IsAuthenticated, IsFollower ]




class ListWhoAmIFollowingView(ListAPIView):
	serializer_class = FollowingAUserSerializer
	permission_classes = [IsAuthenticated, ]


	def get_queryset(self):
		return Relationship.objects.filter(follower=self.request.user)



#########################################

class ListView(ListAPIView):
    serializer_class = CreateEventSerializer

    def get_queryset(self):
        return Event.objects.filter(date__gte=datetime.today())

#########################################

class SpecificView(ListAPIView):
    # queryset = Event.objects.all()
    serializer_class = CreateEventSerializer
    # lookup_field = 'owner__username'
    # lookup_url_kwarg = 'username'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        organizer = User.objects.get(username = self.kwargs['username'])
        return Event.objects.filter(owner=organizer)

#########################################

class SignupView(CreateAPIView):
    serializer_class = SignupSerializer

#########################################

class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        my_data = request.data
        serializer = LoginSerializer(data=my_data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)

########################################




