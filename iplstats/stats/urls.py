from django.urls import path

from . import views
app_name = 'stats'
urlpatterns = [
    path('', views.index, name='index'),
    path('stats_list', views.stats_list, name='stats_list'),
]
