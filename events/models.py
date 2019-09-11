from django.db import models
from django.contrib.auth.models import User

class Event(models.Model) :
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=150)
	date = models.DateField()
	time = models.TimeField()
	num_of_tickets = models.IntegerField()
	description = models.TextField()
	location = models.CharField(max_length=150)
	image = models.ImageField(null=True, blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=3)
	# available_tickets = models.IntegerField()


	def get_booked_tickets(self):
		# test = self.booked_tickets.all()
		# print(test)

		booked = self.booked_tickets.all().values_list('tickets',  flat=True)
		count = 0 
		# print(booked)

		for ticket in booked:
			# print( "printing ticket")

			# print(ticket)
			count += ticket

		return count

	def get_available_tickets(self):
		return self.num_of_tickets - self.get_booked_tickets()	





class Book(models.Model):
	event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='booked_tickets')
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	tickets = models.IntegerField()



class UserProfile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'my_user_profile')
	user_photo = models.ImageField(null=True, blank=True)
	bio = models.TextField()



class Relationship(models.Model):
	following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
	follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')


# class Following (models.Model):
# 	follow = models.ManyToManyField(User, through=ThroughModel,related_name='follow_name', symmetrical=False)

