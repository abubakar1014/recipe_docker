from rest_framework import serializers

from social_media.models import Post

class PostSerializer(serializers.ModelSerializer):
    image = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Post
        fields = ["id", "name", "category", "founder", "description", "image"]
        depth = 1