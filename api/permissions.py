from rest_framework.permissions import BasePermission


class IsEventOwner(BasePermission):
	message = "You must be the planner of this event"

	def has_object_permission(self, request, view, obj):
		if obj.owner == request.user:
			return True
		else:
			return False


class IsFollower(BasePermission):
	message = "You must be following this user"

	def has_object_permission(self, request, view, obj):
		if obj.follower == request.user:
			return True
		else:
			return False


