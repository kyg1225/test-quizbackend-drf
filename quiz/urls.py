#quiz폴더 안에 있는 urls.py는 quiz app에 대한 url을 관리해주는 것
#myapi에 있는 urls.py는 전체 프로젝트에 대한 url을 관리해주는 것
#따라서 quiz의 url을 먼저 설정하고 이것을 myapi의 url에 연결시켜주기

from django.urls import path, include
from .views import helloAPI, randomQuiz

urlpatterns = [
    path("hello/", helloAPI),
    path("<int:id>/", randomQuiz),
]
