from django.urls import path, include
from .views import *

urlpatterns = [
    path("", NormalUserApi.as_view()),
    

]