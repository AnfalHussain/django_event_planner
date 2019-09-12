from rest_framework import serializers
from events.models import Event, Book, Relationship
from django.contrib.auth.models import User




class ListBookedEventsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = ['event', 'tickets',]


class BookEventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = ['tickets',]


class CreateEventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		exclude = ['owner',]



class WhoBookedAnEventSerializer(serializers.ModelSerializer):
	booked_by = serializers.SerializerMethodField()

	class Meta:
		model = Book
		fields = ['booked_by', 'event', 'tickets',]

	def get_booked_by(self, obj):
		return "%s"%(obj.user.username)







class FollowSerializer(serializers.ModelSerializer):

	class Meta:
		model = Relationship
		fields = ['following',]



class FollowingAUserSerializer(serializers.ModelSerializer):

	username = serializers.SerializerMethodField()

	class Meta:
		model = Relationship
		fields = ['username',]

	def get_username(self, obj):
		return "%s"%(obj.following.username)    






# class EventSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Event
#         exclude = ['owner']
#         # fields = '__all__'
# ​

class SignupSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email' ,'password']

	def create(self, validated_data):
		username = validated_data['username']
		first_name = validated_data['first_name']
		last_name = validated_data['last_name']
		email = validated_data['email']
		password = validated_data['password']
		new_user = User(username=username, first_name=first_name, last_name=last_name, email=email)
		new_user.set_password(password)
		new_user.save()
		return validated_data


class LoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField(write_only=True)

	def validate(self, data):
		my_username = data.get('username')
		my_password = data.get('password')

		try:
			user_obj = User.objects.get(username=my_username)
		except:
			raise serializers.ValidationError("This username does not exist")
		if not user_obj.check_password(my_password):
			raise serializers.ValidationError("Incorrect username/password combination! Noob..")
		return data					