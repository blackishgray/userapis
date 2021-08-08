from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserApiModelSerializer

from .models import UserApiModel

# Create your views here.
def index(request):
    mydict = {
        'name':'Rahil'
    }
    return render(request, 'index.html', context = mydict)

#list of all the requests
#present in for the api
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'usersList':'/usersList',
        'userDetial' : '/user-detial/<str:pk>',
        'userCreate' : '/user-create',
        'userUpdate' : '/user-update/<str:pk>',
        'userDelete' : '/user-delete/<str:pk>',
    }
    return Response(api_urls)

#list all the data present in the api
@api_view(['GET'])
def usersList(request):
    users = UserApiModel.objects.all().order_by('-id')
    serializer = UserApiModelSerializer(users, many=True)
    return Response(serializer.data)


#detail of a particular user
#using id
@api_view(['GET'])
def userDetail(request, pk):
    user = UserApiModel.objects.get(id=pk)
    serializer = UserApiModelSerializer(user, many=False)
    return Response(serializer.data)

# filter through using first name 
@api_view(['GET'])
def userFilterFirstName(request, first_name):
    user = UserApiModel.objects.filter(first_name=first_name)
    serializer = UserApiModelSerializer(user, many=True)
    return Response(serializer.data)


# Using last Name filter the data table
@api_view(['GET'])
def userFilterLastName(request, last_name):
    user = UserApiModel.objects.filter(last_name=last_name)
    serializer = UserApiModelSerializer(user, many=True)
    return Response(serializer.data)

# Using age filter the data table
@api_view(['GET'])
def userFilterAge(request, age):
    user = UserApiModel.objects.filter(age=int(age))
    serializer = UserApiModelSerializer(user, many=True)
    return Response(serializer.data)

# .Using date of birth
@api_view(['GET'])
def userFilterDob(request, dob):
    user = UserApiModel.objects.filter(dob=dob)
    serializer = UserApiModelSerializer(user, many=True)
    return Response(serializer.data)


#create a user with the json format
@api_view(['POST'])
def userCreate(request):
    serializer = UserApiModelSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


#update a user data
@api_view(['POST'])
def userUpdate(request, pk):
    user = UserApiModel.objects.get(id=pk)
    serializer = UserApiModelSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

#delete a user with id
@api_view(['DELETE'])
def userDelete(request, pk):
    user = UserApiModel.objects.get(id=pk)
    serializer = UserApiModelSerializer(instance=user, data=request.data)

    user.delete()

    return Response('User Deleted')
