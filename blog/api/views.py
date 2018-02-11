from django_filters.rest_framework import DjangoFilterBackend

from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from .pagination import PostLimitOffsetPagination,PostPageNumberPagination
from rest_framework.generics import (

    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView,
)



from rest_framework.filters import (
SearchFilter,
OrderingFilter
)

from rest_framework.permissions import (
AllowAny,
IsAuthenticated,
IsAdminUser,
IsAuthenticatedOrReadOnly

)

from .permissions import IsOwnerOrReadOnly

from blog.models import Post
from .serializers import PostListSerializer,PostDetailSerializer,PostCreateUpdateSerializer

class PostListAPIView(APIView):

    serializer_class = PostListSerializer
    permission_classes = [AllowAny]
    filter_backends= [SearchFilter,OrderingFilter]
    search_fields=["title","content","user__first_name"]
    pagination_class = PostPageNumberPagination
    renderer_classes = [TemplateHTMLRenderer]
    template_name="base3.html"

    def get_queryset(self,request,*args,**kwargs):
        queryset_list = Post.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query)
            )
        return Response({'profiles':queryset_list})



class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset=Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsOwnerOrReadOnly]


    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsOwnerOrReadOnly]

class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    permission_classes = [AllowAny]
    serializer_class = PostDetailSerializer

class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class =  PostCreateUpdateSerializer
    #permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)