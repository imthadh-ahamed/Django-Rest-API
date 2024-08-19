from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.views import APIView

# Create your views here.

# This view will list all blog posts and create a new blog post
class BlogPostListCreate(generics.ListCreateAPIView):
    # This view will list all blog posts and create a new blog post
    queryset = BlogPost.objects.all()
    # This is the serializer class that will be used to serialize the data
    serializer_class = BlogPostSerializer
    
    # This method will delete all blog posts
    def delete(self, request, *args, **kwargs):
        # This will delete all blog posts
        BlogPost.objects.all().delete()
        # This will return a response with a status code of 204
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# This view will retrieve, update, and destroy a blog post  
class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    # This view will retrieve, update, and destroy a blog post
    queryset = BlogPost.objects.all()
    # This is the serializer class that will be used to serialize the data
    serializer_class = BlogPostSerializer
    lookup_field = "pk"
    
# This view will list all blog posts  
class BlogPostList(APIView):
    # This view will list all blog posts
    def get(self, request, formate=None):
        # This will get the title from the query parameters
        title = request.query_params.get("title", "")
        
        if title:
            # This will filter the blog posts by the title
            blogposts = BlogPost.objects.filter(title__icontains=title)
        else:
            # This will get all blog posts
            blogposts = BlogPost.objects.all()
            
        serializer = BlogPostSerializer(blogposts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)