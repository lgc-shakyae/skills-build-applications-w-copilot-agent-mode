from django.urls import path
from .views import UserList, TeamList, ActivityList, LeaderboardList, WorkoutList
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'teams': reverse('team-list', request=request, format=format),
        'activities': reverse('activity-list', request=request, format=format),
        'leaderboard': reverse('leaderboard-list', request=request, format=format),
        'workouts': reverse('workout-list', request=request, format=format),
    })

urlpatterns = [
    path('', api_root, name='api-root'),
    path('users/', UserList.as_view(), name='user-list'),
    path('teams/', TeamList.as_view(), name='team-list'),
    path('activities/', ActivityList.as_view(), name='activity-list'),
    path('leaderboard/', LeaderboardList.as_view(), name='leaderboard-list'),
    path('workouts/', WorkoutList.as_view(), name='workout-list'),
]
