from django.shortcuts import render, get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Employee
from .permissions import IsSuperUserOrReadOnly
from .serializers import EmployeeSerializer, UserRegistrationSerializer
from rest_framework import status


# Create your views here.
class EmployeeListCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperUserOrReadOnly]

    def get(self,request):
        e=Employee.objects.all()
        serializer_instance=EmployeeSerializer(e,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer_instance=EmployeeSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

class EmployeeRetrieveUpdateDeleteView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperUserOrReadOnly]

    def get(self,request,pk):
        e=get_object_or_404(Employee,id=pk)
        serializer_instance=EmployeeSerializer(e)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        e=get_object_or_404(Employee,id=pk)
        serializer_instance=EmployeeSerializer(e,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        e=get_object_or_404(Employee,id=pk)
        e.delete()
        return Response({'Message':'Employee deleted successfully'},status=status.HTTP_204_NO_CONTENT)


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        serializer_instance=UserRegistrationSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)



