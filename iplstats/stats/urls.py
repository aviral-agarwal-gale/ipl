from django.urls import path

from . import views
app_name = 'stats'
urlpatterns = [
    path('', views.index, name='index'),
    path('stats_list', views.stats_list, name='stats_list'),
    # path('top4', views.top4, name='top4'),
    # path('most_tosses', views.most_tosses, name='most_tosses'),
    # path('max_pom', views.max_pom, name='max_pom'),
    # path('max_matches', views.max_matches, name='max_matches'),
    # path('location', views.location, name='location'),
    # path('per_bat', views.per_bat, name='per_bat'),
    # path('margin', views.margin, name='margin'),
    # path('number', views.number, name='number'),
    # path('toss_match', views.toss_match, name='toss_match'),
    # # path('runs', views.runs, name='runs'),
    # path('catches', views.catches, name='catches'),
]
