from rest_framework import viewsets, permissions

from account.permissions import SecondLevelPermission, FirstLevelPermission
from course import serializers
from course.models import Subject, Course



class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer

    def get_permissions(self):
        if self.action in permissions.SAFE_METHODS:
            return [FirstLevelPermission()]
        return [SecondLevelPermission()]


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = serializers.SubjectSerializer

    def get_permissions(self):
        if self.action in permissions.SAFE_METHODS:
            return [FirstLevelPermission()]
        return [SecondLevelPermission()]
