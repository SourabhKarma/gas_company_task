from rest_framework import permissions


class IsobjectUser(permissions.BasePermission):
    """
    Allows access only to object users.
    """

    def has_permission(self, request, view):
        return bool(request.user)
    



class IsAuthenticatedAndOwner(permissions.BasePermission):
    message = 'You must be the owner of this object.'
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    def has_object_permission(self, request, view, obj):
        return obj.customer == request.user
    

