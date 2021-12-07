from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check if the profile that the user is trying to edit belongs to them"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class PostUserFeed(permissions.BasePermission):
    """Allow logged in users to post into feed"""

    def has_object_permission(self, request, view, obj):
        """Check if the profile that the user is trying to edit belongs to them"""

        if request.method == "POST":
            return request.user.is_authenticated
        elif request.method in permissions.SAFE_METHODS:
            return True
        else:
            print("requester: ",request.user.id)
            print("reqested object: ",obj.user_profile.id)
            return request.user.id == obj.user_profile.id
