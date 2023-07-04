from django.urls import path
from mahalla.views import *

urlpatterns = [
    path('categoriya_people_all_views/',CategoriyaPeopleAllViews.as_view()),
    path('categoriya_people_deteile/<int:pk>/',CategoriyaPeopleDeteile.as_view()),
    path('sektor_employe_views/',SektorEployeViews.as_view()),
    path('people_all_mahalla_views/',PeopleAllMahallaViews.as_view()),
    path('peopele_get_views/<int:pk>/',PeopeleGetViews.as_view()),

    # path('task_all_views/',TaskAllViews.as_view()),
    path('task_categoriya_all/',TaskCategoriyaAll.as_view()),
    path('employe_get_all_views/',EmployeGetAllViews.as_view()),

    path('all_task_views/',AllTAskViews.as_view()),
    path('create_task_files/<int:pk>/',CreateTaskFiles.as_view()),

    path('categoriya_employe_deteile/<int:pk>/',CategoriyaEmployeDeteile.as_view()),
    path('employe_task_files/<int:pk>/',EmployeTaskFiles.as_view()),
    
    path('reagion_employe/<int:pk>/',ReagionEmploye.as_view()),
    path('region_task_files/<int:pk>/',RegionTaskFiles.as_view()),

    # 
    path('district_all_views/',DistrictAllViews.as_view()),
    path('districk_sektor_deteteile/<int:pk>/<int:pkk>/',DistrickSektorDeteile.as_view()),
    path('categoriya_people_views/<int:pk>/<int:id_sektor>/<int:pkk>/',CategoriyaPeopleViews.as_view()),
    path('mahalla_all_views/<int:pk>/<int:pkk>/',MahallaAllViews.as_view()),
    path('mahalla_deteile_views/<int:pk>/<int:id_sektor>/<int:pkk>/',MahallaDeteileViews.as_view()),
    path('mahalla_deteile/<int:id_category>/<int:pk>/<int:id_sektor>/<int:pkk>/',MahallaDeteiles.as_view()),

]