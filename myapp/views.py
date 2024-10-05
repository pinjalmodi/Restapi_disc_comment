from django.shortcuts import render
from rest_framework import generics
from .models import Discussion,Comment
from .serializers import DiscussionSerializer,CommentSerializer
# Create your views here.

class DiscussionList(generics.ListCreateAPIView):
	queryset=Discussion.objects.all()
	serializer_class=DiscussionSerializer


class CommentList(generics.ListCreateAPIView):
	queryset=Comment.objects.all()
	serializer_class=CommentSerializer

class DiscussionDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset=Discussion
	serializer_class=DiscussionSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset=Comment
	serializer_class=CommentSerializer

