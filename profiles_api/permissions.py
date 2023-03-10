#from video 45
from rest_framework import permissions



class UpdateOwnProfile(permissions.BasePermission):
    """allow users to edit their own profile"""


    def has_object_permission(self, request, view, obj):
        """checking user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


#from video 59
class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own profile"""

    def has_object_permission(self, request, view, obj):
        """check the user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
