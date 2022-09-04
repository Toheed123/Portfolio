from msilib.schema import Class
from django.shortcuts import render
from django.http import HttpResponse
# from branch.templates import hello

def hello(request):
    return render(request,'hello.html',{})
    
    
    

# from branch.serializers import dataserializer
# from rest_framework import viewsets
# from rest_framework import permissions
# from branch.models import data



    
# class dataViewSet(viewsets.ModelViewSet):
#     queryset = data.objects.all()
#     serializer_class = dataserializer
#     permission_classes = [permissions.IsAuthenticated]