from rest_framework import serializers
from datetime import date,timedelta
from authen.models import *
from mahalla.models import *

class CategoriyaPeopleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoriya
        fields = ['id','name']

class UserSektorSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustumUsers
        fields = ['id','first_name','last_name','position','phone']

class RegionAllSerializers(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id','name']

class MahallaAllSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mahalla
        fields = ['id','name','id_sektor']



class SektorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sektor
        fields = ['id','name']

class DistirckSerializers(serializers.ModelSerializer):
    id_sektor = SektorSerializers(read_only=True,many=True)
    class Meta:
        model = District
        fields = ['id','name','id_sektor']

class TaslCategoriyaSerializers(serializers.ModelSerializer):
    class Meta:
        model = TaskCategoriya
        fields = '__all__'

class TaskPeopleSerializers(serializers.ModelSerializer):
    id_user = UserSektorSerializers(read_only=True)
    id_task_category = TaslCategoriyaSerializers(read_only=True)
    class Meta:
        model = Tasks
        fields = '__all__'

class PeopleAllSerializers(serializers.ModelSerializer):
    id_categor = CategoriyaPeopleSerializers(read_only=True)
    responsible_employee = UserSektorSerializers(read_only=True)
    id_mahalla = MahallaAllSerializers(read_only=True)
    id_region = RegionAllSerializers(read_only=True)
    id_sektor = SektorSerializers(read_only=True)
    id_districk = DistirckSerializers(read_only=True)
    people = TaskPeopleSerializers(many=True,read_only=True)
    class Meta:
        model = People
        fields = ('id','full_name','birth_date','phone','village','additional_information','id_categor','id_mahalla','id_sektor','id_region','id_districk','responsible_employee','create_user','people')

class PeopleCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ['full_name','birth_date','phone','village','additional_information','id_categor','id_mahalla','id_sektor','id_region','id_districk','responsible_employee','create_user',]
    def create(self, validated_data):
        user_create = People.objects.create(**validated_data)
        user_create.id_mahalla = self.context.get('id_mahalla')
        user_create.id_sektor = self.context.get('id_sektor')
        user_create.id_region = self.context.get('id_region')
        user_create.id_districk = self.context.get('id_districk')
        user_create.create_user = self.context.get('create_user')
        user_create.save()
        return user_create
    



class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = TaskCategoriya
        fields = ['id','name']

class TaskUser(serializers.ModelSerializer):
    class Meta:
        model = CustumUsers
        fields = ['id','first_name','last_name','phone','position']

class UserSerializersAll(serializers.ModelSerializer):
    class Meta:
        model = CustumUsers
        fields = ['id','first_name','last_name']

class TaskAllSerializers(serializers.ModelSerializer):
    id_user = TaskUser(read_only=True)
    class Meta:
        model = Tasks
        fields = '__all__'


class TaskCrudSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id','id_people','id_task_category','id_user','task','is_user','comment','date_line']
    def create(self, validated_data):
        task_create = Tasks(
            id_task_category = validated_data['id_task_category'],
            id_user = validated_data['id_user'],
            task = validated_data['task'],
            comment = validated_data['comment']
        )
        task_create.id_people = self.context.get('id_people')
        for item in TaskCategoriya.objects.all():
            if validated_data['id_task_category'] == item:
                x = date.today()+timedelta(days=item.date)
        task_create.date_line = x
        task_create.save()
        return task_create
    
class TaskCreateFiles(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id','id_people','files','is_user','is_task']
    def update(self, instance, validated_data):
        instance.files = validated_data.get('files',instance.files)
        instance.is_user = validated_data.get('is_user',instance.is_user)
        instance.save() 
        return instance