from rest_framework import permissions

class IsStudent(permissions.BasePermission):
    """
    Allows access only to users with student role.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_student)


class IsTourGuide(permissions.BasePermission):
    """
    Allows access only to users with tour guide role.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_tourGuide)


class IsStudentOrTourGuide(permissions.BasePermission):
    """
    Allows access only to users with student role.
    """

    def has_permission(self, request, view):
        return bool(request.user and (request.user.is_student or request.is_tourGuide))