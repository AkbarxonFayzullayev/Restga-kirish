# from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# from .models import *
from .serializers import *


@api_view(["GET", "POST"])
def movie_api(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT", "PATCH", "DELETE"])
def movie_detail(request, slug):
    try:
        movie = Movie.objects.get(slug=slug)
    except Movie.DoesNotExist:
        return Response({"success": False, "error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)

    response = {"success": True}

    if request.method == "PUT":
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response["data"] = serializer.data
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PATCH":
        serializer = MovieSerializer(movie, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response["data"] = serializer.data
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        movie.delete()
        return Response({"success": True, "message": "Movie deleted"}, status=status.HTTP_204_NO_CONTENT)

@api_view(["GET", "POST"])
def actor_list(request):
    if request.method == "GET":
        actors = Actors.objects.all()
        serializer = ActorSerializer(actors, many=True)
        return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def actor_detail(request, slug):
    try:
        actor = Actors.objects.get(slug=slug)
    except Actors.DoesNotExist:
        return Response({"success": False, "error": "Actor not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ActorSerializer(actor)
        return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = ActorSerializer(actor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PATCH":
        serializer = ActorSerializer(actor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        actor.delete()
        return Response({"success": True, "message": "Actor deleted"}, status=status.HTTP_204_NO_CONTENT)
