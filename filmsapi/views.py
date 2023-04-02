from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Actors,Movies,MoviesActors

from .serializers import ActorsSerializer,MoviesSerializer
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser

# Create your views here.
@api_view(['GET','POST'])
def Movies_list (request):
        
        if request.method=='GET':
            filmsapi=Movies.objects.all()
            serializer=MoviesSerializer(filmsapi,many=True)
            return JsonResponse(serializer.data,safe=False)
  
        elif request.method=='POST':
          data=JSONParser().parse(request)
          serializer=MoviesSerializer(data=data)
        if serializer.is_valid():
           serializer.save()
           return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.error,status=400)
# actors_list
@api_view(['GET','POST'])
def Actors_list (request):
    if request.method=='GET':
        
      apis=Actors.object.all()
      serializer=ActorsSerializer(apis,many=True)
      return JsonResponse(serializer.data)
  
    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=ActorsSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data,status=201)
    return JsonResponse(serializer.error,status=400)

@api_view(['GET','POST','DELETE'])
def Movies_details(request,pk):
    try:
        Movies=Movies.object.all(pk=pk)
    except Movies.DoesnotExist:
        return JsonResponse(status=404)
    if request.method=='GET':
        serializer=MoviesSerializer(Movies)
        return JsonResponse(serializer.data)
    elif request.method=='PUT':
        data=JSONParser().parse(request)
        serializer=MoviesSerializer(Movies,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)
    elif request.method=='DELETE':
        Movies.delete()
        return JsonResponse(status=204)
