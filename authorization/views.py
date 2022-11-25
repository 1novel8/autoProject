from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserRegistrationSerializer


class RegistrationUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            print(request.data)
            return redirect('../../customer/'+str(request.data['customer_id'].value))
        else:
            data = serializer.errors
            return Response(data)
