from dataclasses import field
from xml.sax.xmlreader import InputSource
from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        #fields = ['id', 'CompanyName', 'emailId', 'CompanyCode','Strength','webSite','createdTime']
        fields ='__all__'