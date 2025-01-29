from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """
    Custom permission to only allow admins to access the view.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin

class IsManager(permissions.BasePermission):
    """
    Custom permission to only allow managers to access the view.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_manager

class IsEmployee(permissions.BasePermission):
    """
    Custom permission to only allow employees to access the view.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_employee

class IsAdminOrManager(permissions.BasePermission):
    """
    Custom permission to allow both admins and managers to access the view.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.is_admin or request.user.is_manager)

class IsAdminOrEmployee(permissions.BasePermission):
    """
    Custom permission to allow both admins and employees to access the view.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.is_admin or request.user.is_employee)