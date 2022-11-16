
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("delete-user", DestroyUser, basename="destroy")

urlpatterns = [
    path("", UserApi.as_view()),
    # path("get-domain", GetDomain.as_view())
    path("", include(router.urls))
    

]