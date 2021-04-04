from rest_framework import permissions


class UpdateOwnPost(permissions.BasePermission):
    message = "Bro You Must Be Author"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
