# from django.shortcuts import render
from rest_framework import generics
from .serializers import EmployeeSerializer
from .models import Employee

class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

