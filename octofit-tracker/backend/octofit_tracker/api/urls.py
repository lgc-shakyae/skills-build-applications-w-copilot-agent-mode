from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserList, TeamList, ActivityList, LeaderboardList, WorkoutList
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os

@api_view(['GET'])
def api_root(request, format=None):
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        base_url = f"https://{codespace_name}-8000.app.github.dev/api/"
    else:
        base_url = "http://localhost:8000/api/"
    return Response({
        'users': base_url + 'users/',
        'teams': base_url + 'teams/',
        'activities': base_url + 'activities/',
        'leaderboard': base_url + 'leaderboard/',
        'workouts': base_url + 'workouts/',
    })

router = DefaultRouter()
router.register(r'users', UserList, basename='user')
router.register(r'teams', TeamList, basename='team')
router.register(r'activities', ActivityList, basename='activity')
router.register(r'leaderboard', LeaderboardList, basename='leaderboard')
router.register(r'workouts', WorkoutList, basename='workout')

urlpatterns = [
    path('', api_root, name='api-root'),
    path('', include(router.urls)),
]
