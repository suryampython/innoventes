from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from .serializers import CompanySerializer
from .models import Company


class Company_all(APIView):

    def get(self,request):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanySinglecud(APIView):

    def get_object(self,id):
        try:
            return Company.objects.get(id=id)
        except Company.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        company=self.get_object(id)
        serializer = CompanySerializer(company)
        try:
            return Response(serializer.data)
        except:
           return Response(status=status.HTTP_404_NOT_FOUND) 

    def put(self,request,id):
        company=self.get_object(id)
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        company=self.get_object(id)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CompanyPagenation(ListAPIView):
    queryset= Company.objects.all()
    serializer_class = CompanySerializer    
    #def get(self,request):
       # company = Company.objects.all()
       # serializer = CompanySerializer(company)
       # return Response(serializer)
        