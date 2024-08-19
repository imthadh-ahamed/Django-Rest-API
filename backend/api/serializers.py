from rest_framework import serializers
from .models import BlogPost

# This is the serializer class that will be used to serialize the data
class BlogPostSerializer(serializers.ModelSerializer):
    # This is the model that the serializer will serialize
    class Meta:
        # This is the model that the serializer will serialize
        model = BlogPost
        fields = ["id", "title", "content", "published_date"]