from django.urls import path
from . import views

app_name='api'

urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),
    path('usersList', views.usersList, name='usersList'),
    path('userDetail/<str:pk>', views.userDetail, name='userDetail'),
    path('userFilterFirstName/<str:first_name>', views.userFilterFirstName, name='userFilterFirstName'),
    path('userFilterLastName/<str:last_name>', views.userFilterLastName, name='userFilterLastName'), 
    path('userFilterAge/<str:age>', views.userFilterAge, name='userFilterAge'),
    path('userFilterDob/<str:dob>', views.userFilterDob, name='userFilterDob'),
    path('userCreate', views.userCreate, name='userCreate'),
    path('userUpdate/<str:pk>', views.userUpdate, name='userUpdate'),
    path('userDelete/<str:pk>', views.userDelete, name='userDelete'),
]
