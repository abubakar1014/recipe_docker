from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from django.test import RequestFactory
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated,AllowAny
from social_media.models import Post
from social_media.serializers import PostSerializer
from social_media.utils import validate_password, serializer_errors, InvalidException, CustomPagination


        
        
        
class PostView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()

    def post(self, request):
        serializer = PostSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            message = "Post created successfully"
            status_code = status.HTTP_201_CREATED
            return Response({"detail": message}, status_code)
        else:
            data = serializer_errors(serializer)
            raise InvalidException(data)
        
class PostDetailView(APIView):

    def get(self, request, pk):
        queryset = Post.objects.filter(pk=pk).first()
        serializer = PostSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        queryset = Post.objects.filter(pk=pk).first()
        serializer = PostSerializer(queryset, request.data)

        if serializer.is_valid():
            serializer.save()

            message = "Post updated successfully!"
            status_code = status.HTTP_200_OK
        else:
            message = serializer.errors
            status_code = status.HTTP_406_NOT_ACCEPTABLE
        return Response(message, status=status_code)

    def delete(self, request, pk):
        Post.objects.filter(pk=pk).delete()
        return Response("Post deleted successfully", status=status.HTTP_200_OK)