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
from .serializers import (
    UserSerializer,
    AdminSerializer,
    TrainerSerializer,
    ClientSerializer,
)
from django.contrib.auth.hashers import make_password
from datetime import datetime, timedelta
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from datetime import datetime, timedelta
#import jwt
#import jwt

@api_view(["GET"])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getUser(request, pk):
    user = get_object_or_404(User, pk=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


# #add user
# @api_view(['POST'])
# def addUser(request):
#     serializer = UserSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)


@api_view(["POST"])
def addUser(request):
    # Hash the password before saving
    request.data["password"] = make_password(request.data["password"])

    # Initialize the User serializer with request data
    user_serializer = UserSerializer(data=request.data)

    if user_serializer.is_valid():
        # Save the User instance
        user = user_serializer.save()

        # Based on the user_role, create the corresponding role instance
        user_role = request.data["user_role"]
        if user_role == "admin":
            The_Admin.objects.create(user=user)
        elif user_role == "trainer":
            The_Trainer.objects.create(user=user)
        elif user_role == "client":
            The_Client.objects.create(user=user)

        return Response(user_serializer.data)
    else:
        return Response(user_serializer.errors, status=400)


@api_view(["PUT"])
def updateUser(request, pk):
    user = get_object_or_404(User, pk=pk)
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def deleteUser(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return Response("Item successfully deleted!")


@api_view(["GET"])
def getAdmin(request):
    admin = The_Admin.objects.all()
    serializer = AdminSerializer(admin, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getTrainer(request):
    trainer = The_Trainer.objects.all()
    serializer = TrainerSerializer(trainer, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getClient(request):
    client = The_Client.objects.all()
    serializer = ClientSerializer(client, many=True)
    return Response(serializer.data)


def generate_jwt_token(user):
    # Create a new refresh token for the user
    refresh = RefreshToken.for_user(user)

    # Access the access token directly from the refresh token
    access_token = refresh.access_token

    # Custom payload claims
    # Note: The 'exp' claim is automatically managed by SimpleJWT, but you can adjust it if needed
    access_token['user_id'] = user.id
    access_token['email'] = user.email
    access_token['user_role'] = user.user_role
    access_token.set_exp(lifetime=timedelta(days=1))

    return {
        'refresh': str(refresh),
        'access': str(access_token),
    }


def authenticate(email=None, password=None):
    User = get_user_model()
    try:
        user = User.objects.get(email=email)
        if check_password(password, user.password):
            return user
        else:
            return None
    except User.DoesNotExist:
        return None


# Example login view
@api_view(["POST"])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")

    # Perform authentication and get user
    user = authenticate(email=email, password=password)
    if user:
        # Generate JWT token with user role included in the payload
        token = generate_jwt_token(user)
        return Response({"token": token})
    else:
        return Response(
            {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )
