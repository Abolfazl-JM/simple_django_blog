from rest_framework import serializers
from Blog.models import Posts

class post_serializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = "__all__"
