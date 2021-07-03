from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User,Group

class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']

class UserSerializer(serializers.ModelSerializer):
    groups = GroupsSerializer(read_only = True, many = True)
    class Meta:
        model = User
        fields = ['id','email', 'username', 'is_staff', 'is_superuser', 'groups']