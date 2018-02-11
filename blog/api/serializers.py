from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
)
from comments.api.serializers import CommentSerializer
from comments.models import Comment
from blog.models import Post
from accounts.api.serializers import UserDetailSerializer
Post_Detail_url = HyperlinkedIdentityField(
    view_name="posts-api:detail",
    lookup_field="pk",
)
class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model=Post
        fields=[
            "title",
            "content",
            "timestamp",

        ]

class PostDetailSerializer(ModelSerializer):
    url=Post_Detail_url
    user=UserDetailSerializer()
    image=SerializerMethodField()
    html=SerializerMethodField()
    comments=SerializerMethodField()
    class Meta:
        model=Post
        fields=[
            "url",
            "id",
            "user",
            "html",
            "image",
            "title",
            "content",
            "timestamp",
            "comments",

        ]
    def get_html(self,obj):
        return obj.get_markdown()




    def get_image(self,obj):
        try:
            image=obj.image.url
        except:
            image=None

        return image

    def get_comments(self,obj):
        content_type = obj.get_content_type
        object_id = obj.id
        c_qs = Comment.objects.filter_by_instance(obj)
        comments = CommentSerializer(c_qs, many=True).data
        return comments



class PostListSerializer(ModelSerializer):
    user=UserDetailSerializer()
    url=Post_Detail_url
    delete_url=HyperlinkedIdentityField(
        view_name="posts-api:delete",
        lookup_field='pk'
    )


    class Meta:
        model=Post
        fields=[
            "url",
            "user",
            "title",
            "content",
            "timestamp",
            "delete_url",

        ]








