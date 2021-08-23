"""
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.permissions import (IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import(
    CreateAPIView, DestroyAPIView,
    ListAPIView, UpdateAPIView,
    RetrieveAPIView, RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView
)

from .models import WebsiteCrawlRequest
from .permissions import IsOwnerOrReadOnly, IsOwner
from .serializers import WebsiteCrawlCreateUpdateSerializer

class CreateWebsiteCrawlAPIView(APIView):
    queryset = Post.objects.all()
    serializer = WebsiteCrawlCreateUpdateSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, *args, **kwargs):
        serializer = WebsiteCrawlCreateUpdateSerializer
        if serializer.is_valid(raise_exception = True):
            serializer.save(author = request.user)
            return Response(serializer.data, status = 200)
        else:
            return Response({"errors": serializer.errors}, status = 400)
"""
