from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers import CustomUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
# from django.contrib.auth import authenticate


class CustomUserCreate(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = CustomUserSerializer

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class LoginView(GenericAPIView):
#     permission_classes = [AllowAny]
#     serializer_class = LoginSerializer

#     def post(self, request):
#         data = request.data
#         print(data)
#         user_name = data.get('user_name', '')
#         password = data.get('password', '')
#         print(user_name, password)
#         # print(getattr(user_name, 'is_active', None))
#         user = authenticate(username=user_name, password=password)

#         if user:
#             auth_token = jwt.encode(
#                 {'user_name': user.user_name}, settings.JWT_SECRET_KEY, algorithm="HS256")
#             serializer = CustomUserSerializer(user)
#             data = {'user': serializer.data, 'token': auth_token}
#             return Response(data, status=status.HTTP_200_OK)
#             # SEND RES
#         return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
