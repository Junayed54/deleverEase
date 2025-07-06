from rest_framework.permissions import BasePermission, SAFE_METHODS

# class IsAdmin(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_authenticated and request.user.role == 'admin'




class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        # Allow safe methods for everyone but restrict others to admin
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role == 'admin'
    
    
class IsDeliveryMan(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'delivery'


class IsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'user'


class IsOwner(BasePermission):
    """
    Object-level permission to only allow users to access their own object.
    """
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
