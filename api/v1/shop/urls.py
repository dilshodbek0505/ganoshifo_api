from django.urls import path
from .views import (
    AboutApi,
    BannerApi,
    CategoryApi,
    ClientApi,
    FileApi,
    InstructionApi,
    ProductApi,
    MemberApi,
    ResultApi,
    LessonApi,
    OneLessonApi
)

urlpatterns = [
    path("lesson/",LessonApi.as_view()),
    path("about/", AboutApi.as_view()),
    path("banner/", BannerApi.as_view()),
    path("category/", CategoryApi.as_view()),
    path("client/", ClientApi.as_view()),
    path("file/", FileApi.as_view()),
    path("instruction/", InstructionApi.as_view()),
    path("product/", ProductApi.as_view()),
    path("member/", MemberApi.as_view()),
    path("result/", ResultApi.as_view()),
    path("lesson/<int:pk>/", OneLessonApi.as_view())
]
