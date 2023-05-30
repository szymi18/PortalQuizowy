from django.urls import path, include
from rest_framework import routers

from . import views_api

# Router do widoków w API
api_router = routers.DefaultRouter()

api_router.register('users', views_api.UserViewSet)
api_router.register('Quiz', views_api.QuizViewSet)
api_router.register('Question', views_api.QuestionViewSet)


urlpatterns = [
    path('api/', include(api_router.urls)),
    path('/api/questions', include(api_router.urls)),
    path('/api/Quiz', include(api_router.urls))
]