from rest_framework import serializers
from rest_framework import authentication as auth
from rest_framework import permissions as perm

from . import models
from project.users.models import User
from django.conf import settings


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Member
        fields = '__all__'