from rest_framework.response import Response
from rest_framework import  status
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.permissions import IsAuthenticated
from authen.renderers import UserRenderers
from rest_framework.parsers import MultiPartParser, FormParser
from mahalla.models import *
from authen.models import *
from mahalla.serializers import *

class CategoriyaPeopleAllViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self,request,format=None):
        objects_list = Categoriya.objects.all()
        serizalizers = CategoriyaPeopleSerializers(objects_list,many=True)
        return Response(serizalizers.data,status=status.HTTP_200_OK)

class TaskCategoriyaAll(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self,request,format=None):
        objects_list = TaskCategoriya.objects.all()
        serizalizers = TaslCategoriyaSerializers(objects_list,many=True)
        return Response(serizalizers.data,status=status.HTTP_200_OK)

class EmployeGetAllViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self,request,format=None):
        objects_list = CustumUsers.objects.filter(id_mahalla=request.user.id_mahalla)
        serizalizers = UserSektorSerializers(objects_list,many=True)
        return Response(serizalizers.data,status=status.HTTP_200_OK)
    
class CategoriyaPeopleDeteile(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self,request,pk,format=None):
        objects_list = People.objects.filter(id_categor__id=pk,people__id_user=request.user.id)
        print(Tasks.objects.check_deadline_taks(request.user.id,pk))
    
        serizalizers = PeopleAllSerializers(objects_list,many=True)
        return Response(serizalizers.data,status=status.HTTP_200_OK)

class AllTAskViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self,request,format=None):
        objects_list = People.objects.filter(id_mahalla=request.user.id_mahalla)
        serizalizers = PeopleAllSerializers(objects_list,many=True)
        return Response(serizalizers.data,status=status.HTTP_200_OK)

class SektorEployeViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self,request,format=None):
        objects_list = CustumUsers.objects.filter(id_districk=request.user.id_districk,groups__name__in = ['sektor'])
        serizalizers = UserSektorSerializers(objects_list,many=True)
        return Response(serizalizers.data,status=status.HTTP_200_OK)
    
class PeopleAllMahallaViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self,request,format=None):
        objects_list = People.objects.filter(create_user=request.user)
        serizalizers = PeopleAllSerializers(objects_list,many=True)
        return Response(serizalizers.data,status=status.HTTP_200_OK)
    def post(self,request,format=None):
        mahalla = request.user.id_mahalla
        sektor = request.user.id_sektor
        disreick = request.user.id_districk
        region = request.user.id_region
        create = request.user
        serializers = PeopleCreateSerializers(data=request.data,context={'id_mahalla':mahalla,'id_sektor':sektor,'id_region':region,'id_districk':disreick,'create_user':create})
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


class PeopeleGetViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self,request,pk,format=None):
        objects_list = People.objects.filter(id=pk).order_by('-pk')
        serizalizers = PeopleAllSerializers(objects_list,many=True)
        return Response(serizalizers.data,status=status.HTTP_200_OK)
    def post(self,request,pk,format=None):
        lists = People.objects.get(id=pk)
        serializers = TaskCrudSerializers(data=request.data,context={'id_people':lists})
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


class CreateTaskFiles(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self,request,pk,format=None):
        instance=Tasks.objects.filter(id_people__id=pk,id_user__id=request.user.id)
        serizalizers = TaskAllSerializers(instance,many=True)
        return Response(serizalizers.data,status=status.HTTP_200_OK)
    def put(self,request,pk,format=None):
        serializers = TaskCreateFiles(instance=Tasks.objects.filter(id_people__id=pk)[0],data=request.data,partial =True)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data,status=status.HTTP_200_OK)
        return Response({'error':'update error data'},status=status.HTTP_400_BAD_REQUEST)


class CategoriyaEmployeDeteile(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self,request,pk,format=None):
        objects_list = People.objects.filter(id_categor__id=pk,responsible_employee__id=request.user.id)
        serizalizers = PeopleAllSerializers(objects_list,many=True)
        return Response(serizalizers.data,status=status.HTTP_200_OK)

class EmployeTaskFiles(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self,request,pk,format=None):
        instance=Tasks.objects.filter(id_people__id=pk,id_people__responsible_employee__id=request.user.id)
        serizalizers = TaskAllSerializers(instance,many=True)
        return Response(serizalizers.data,status=status.HTTP_200_OK)
    def put(self,request,pk,format=None):
        serializers = TaskCreateFiles(instance=Tasks.objects.filter(id_people__id=pk,id_people__responsible_employee__id=request.user.id)[0],data=request.data,partial =True)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data,status=status.HTTP_200_OK)
        return Response({'error':'update error data'},status=status.HTTP_400_BAD_REQUEST)
    
class ReagionEmploye(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self,request,pk,format=None):
        objects_list = People.objects.filter(id_categor__id=pk,id_region=request.user.id_region)
        serizalizers = PeopleAllSerializers(objects_list,many=True)
        return Response(serizalizers.data,status=status.HTTP_200_OK)
    
class RegionTaskFiles(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self,request,pk,format=None):
        instance=Tasks.objects.filter(id_people__id=pk,id_people__id_region=request.user.id_region)
        serizalizers = TaskAllSerializers(instance,many=True)
        return Response(serizalizers.data,status=status.HTTP_200_OK)
# class TaskAllViews(APIView):
#     render_classes = [UserRenderers]
#     perrmisson_class = [IsAuthenticated]
#     def get(self,request,format=None):
#         objects_list = Tasks.objects.all()
#         serizalizers = TaskAllSerializers(objects_list,many=True)
#         return Response(serizalizers.data,status=status.HTTP_200_OK)
    # def post(self,request,format=None):
    #     serializers = TaskCrudSerializers(data=request.data)
    #     if serializers.is_valid(raise_exception=True):
    #         serializers.save()
    #         return Response(serializers.data,status=status.HTTP_201_CREATED)
    #     return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)