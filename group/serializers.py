from django.contrib.auth import get_user_model
from rest_framework import serializers
from course.models import Course
from group.models import Group

User = get_user_model()


class GroupSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())
    mentor = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())

    class Meta:
        model = Group
        fields = ['id', 'title', 'students', 'mentor', 'course']
