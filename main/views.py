# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import User
# from .serializers import UserSerializer

# # Create your views here.

# #get all users
# @api_view(['GET'])
# def getUsers(request):
#     users = User.objects.all()
#     serializer = UserSerializer(users, many=True)
#     return Response(serializer.data)

# #get single user
# @api_view(['GET'])
# def getUser(request, pk):
#     user = User.objects.get(id=pk)
#     serializer = UserSerializer(user, many=False)
#     return Response(serializer.data)

# #add user
# @api_view(['POST'])
# def addUser(request):
#     serializer = UserSerializer(data=request.data)
    
#     if serializer.is_valid():
#         serializer.save()
    
#     return Response(serializer.data)

# #update user
# @api_view(['PUT'])
# def updateUser(request, pk):
#     user = User.objects.get(id=pk)
#     serializer = UserSerializer(instance=user, data=request.data)
    
#     if serializer.is_valid():
#         serializer.save()
    
#     return Response(serializer.data)

# #delete user
# @api_view(['DELETE'])
# def deleteUser(request, pk):
#     user = User.objects.get(id=pk)
#     user.delete()
    
#     return Response('Item successfully deleted!')
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, The_Admin, The_Trainer, The_Client
from .serializers import UserSerializer, AdminSerializer, TrainerSerializer, ClientSerializer
from django.contrib.auth.hashers import make_password

@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUser(request, pk):
    user = get_object_or_404(User, pk=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addUser(request):
    modified_request_data = request.data.copy()
    modified_request_data['password'] = make_password(request.data['password'])
    serializer = UserSerializer(data=modified_request_data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def updateUser(request, pk):
    user = get_object_or_404(User, pk=pk)
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteUser(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return Response('Item successfully deleted!')

@api_view(['GET'])
def getAdmin(request):
    admin = The_Admin.objects.all()
    serializer = AdminSerializer(admin, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTrainer(request):
    trainer = The_Trainer.objects.all()
    serializer = TrainerSerializer(trainer, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getClient(request):
    client = The_Client.objects.all()
    serializer = ClientSerializer(client, many=True)
    return Response(serializer.data)
