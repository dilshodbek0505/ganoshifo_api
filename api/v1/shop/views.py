from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from .serializers import (
    AboutSerializer,
    BannerSerializer,
    CategorySerializer,
    ClientSerializer,
    FileSerialize,
    InstructionSerializer,
    MemberSerializer,
    ResultSerializer,
    ProductSerializer,
    LessonSerialize
)
from .models import (
    About,
    Banner,
    Category,
    Client,
    File,
    Instruction,
    Product,
    Result,
    Member,
    Lesson
)
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class OneLessonApi(APIView):
    def get(self, request, pk, *args, **kwargs):
        lesson = Lesson.objects.filter(id = pk).first()
        if lesson == []:
            return Response({
                "status": True,
                "data": "Not found"
            })
        serializer = LessonSerialize(lesson)
        return Response({
            "status": True,
            "data": serializer.data
        }) 

class LessonApi(ListAPIView):
    serializer_class = LessonSerialize
    queryset = Lesson.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    pagination_class = LimitOffsetPagination


class ProductApi(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.select_related("category_id").all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category_id__name', 'id']
    pagination_class = None

class ResultApi(ListAPIView):
    serializer_class = ResultSerializer
    queryset = Result.objects.select_related("product_id").all()
    pagination_class = None


class MemberApi(ListCreateAPIView):
    serializer_class = MemberSerializer
    queryset = Member.objects.select_related("client_id").all()
    pagination_class = None

class AboutApi(ListAPIView):
    serializer_class = AboutSerializer
    queryset = About.objects.all()
    pagination_class = None

class BannerApi(ListCreateAPIView):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    pagination_class = None

class CategoryApi(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = None

class ClientApi(ListCreateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.select_related("product_id").all()
    pagination_class = None

class FileApi(ListCreateAPIView):
    serializer_class = FileSerialize
    queryset = File.objects.select_related("banner_id", "product_id", "result_id", "instruction_id", "about_id").all()
    pagination_class = None

class InstructionApi(ListAPIView):
    serializer_class = InstructionSerializer
    queryset = Instruction.objects.select_related('product_id').all()
    pagination_class = None
