from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .serializers import WatchListserializer

from .models import WatchList,Platform
from rest_framework.decorators import api_view

@api_view(['GET'])
def movie_list(request):
    movie_list = WatchList.objects.all()
    lists = WatchListserializer(movie_list, many=True)
    return Response(lists.data)

@api_view(['GET', 'POST'])
def movie(request, pk):
    if request.method == 'GET':
        movie = WatchList.objects.get(id=pk)
        movielizer = WatchListserializer(movie, many=False)
        return Response(movielizer.data)
    elif request.method == 'POST':
        movielizer = WatchListserializer(data=request.data)
        if movielizer.is_valid():
            movielizer.save()
            return Response(movielizer.data, status=status.HTTP_201_CREATED)
        return Response(movielizer.errors, status=status.HTTP_400_BAD_REQUEST)

