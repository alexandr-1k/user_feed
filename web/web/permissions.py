from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):

        if view.action in ('list', 'retrieve'):
            return True
        else:
            # if user is the author
            return request.user.is_authenticated and request.user.role == "A"

    def has_object_permission(self, request, view, obj):

        if view.action in ('list', 'retrieve'):
            return True

        if view.action == 'create':
            # if user is the author
            return request.user.role == 'A'

        if view.action in ('update', 'partial_update', 'destroy'):
            return request.user == obj.author

        return False
