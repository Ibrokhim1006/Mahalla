from django.contrib.auth.models import User,Group
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
from authen.models import *


class UserGroupSerizliers(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id','name']

class SektorAllSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sektor
        fields = '__all__'

class RegionAllSerializers(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class DistrikAllSerializers(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id','name']

class MahallaAllSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mahalla
        fields = ['id','name']

class UserSiginInSerializers(serializers.ModelSerializer):
    username = serializers.CharField(max_length=250)
    class Meta:
        model = CustumUsers
        fields = ['username','password']
class UserCreateSerializers(serializers.ModelSerializer): 
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = CustumUsers
        fields = ['username','first_name','last_name','phone','position','id_sektor','id_region','id_districk','id_mahalla','groups','password','password2']
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs
    def create(self,validated_data):
        client_create = CustumUsers.objects.create_user(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            username = validated_data['username'],
            phone = validated_data['phone'],
            position = validated_data['position'],
            id_sektor = validated_data['id_sektor'],
            id_region = validated_data['id_region'],
            id_districk = validated_data['id_districk'],
            id_mahalla = validated_data['id_mahalla'],
        )
        client_create.set_password(validated_data['password'])
        for i in validated_data['groups']:
            client_create.groups.add(i.id)
        client_create.save()
        return client_create
class UserInformationSerializers(serializers.ModelSerializer):
    groups = UserGroupSerizliers(read_only = True,many=True)
    id_sektor = SektorAllSerializers(read_only = True)
    id_region = RegionAllSerializers(read_only = True)
    id_districk = DistrikAllSerializers(read_only = True)
    id_mahalla = MahallaAllSerializers(read_only = True)
    class Meta:
        model = CustumUsers
        fields = ['username','first_name','last_name','phone','position','id_sektor','id_region','id_districk','id_mahalla','groups',]