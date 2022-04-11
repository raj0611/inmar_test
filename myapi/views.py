

#
# from rest_framework import viewsets
#
# from .serializers import EmpSerializer
# from .models import Emp
#
#
# class HeroViewSet(viewsets.ModelViewSet):
#     queryset = Emp.objects.all().order_by('location')
#     serializer_class = EmpSerializer



import json

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from . import models

from .serializers import EmpSerializer


@api_view(['GET', 'POST'])
def emp_list(request):

    if request.method == 'GET':
        emp = models.Emp.objects.all()
        serializer = EmpSerializer(emp, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EmpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def emp_detail(request, pk):

    try:
        emp = models.Emp.objects.get(pk=pk)
    except models.Emp.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmpSerializer(emp)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmpSerializer(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''
a. /api/v1/location,
b. /api/v1/location/{location_id}/department
c. /api/v1/location/{location_id}/department/{department_id}/category

'''


