from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticated
from user.serializers import CustomerSerializer, EmployeeSerializer
from user.models import (
    User,
    Customer,
    Client,
    Employee,
)


class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_customer or request.user.is_staff


class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_employee or request.user.is_staff


class CustomerInfo(APIView):
    permission_classes = [IsAuthenticated & IsCustomer]

    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        customer = self.get_object(request.user.id)
        serializer = CustomerSerializer(customer.to_dict())
        return Response(serializer.data)


class EmployeeInfo(APIView):
    permission_classes = [IsAuthenticated & IsEmployee]

    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        employee = self.get_object(request.user.id)
        serializer = EmployeeSerializer(employee.to_dict())
        return Response(serializer.data)
