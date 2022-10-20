from django.shortcuts import render, get_object_or_404, redirect
from .models import Deliveries, Matches
from django.db.models import Count, Max, F

from django.http import HttpResponse

def index(request):

    return render(request, "index.html")

def stats_list(request):
    year = request.POST.get("year")
    t4 = top4(year)
    mt = most_tosses(year)
    mp = max_pom(year)
    mm = max_matches(year)
    l = location(year)
    pb = per_bat(year)
    m = margin(year)
    n = number(year)
    tm = toss_match(year)
    return render(request, "stats_list.html", {'year': year,'top4': t4, 'most_tosses': mt, 'max_pom': mp, "max_matches": mm, 'location': l, 'per_bat': pb, 'margin': m, 'number': n, 'toss_match': tm})    

def top4(year):
    match = Matches.objects.filter(season = year).values('winner').order_by().annotate(winner_count = Count('winner')).order_by('-winner_count')[:4]

    return list(match)

def most_tosses(year):
    match = Matches.objects.filter(season = year).values('toss_winner').order_by().annotate(winner_count = Count('toss_winner')).order_by('-winner_count')[:1]
    # print(match)
    return list(match)

def max_pom(year):
    match = Matches.objects.filter(season = year).values('player_of_match').order_by().annotate(winner_count = Count('player_of_match')).order_by('-winner_count')[:1]
    # print(match)
    return list(match)

def max_matches(year):
    match = Matches.objects.filter(season = year).values('winner').order_by().annotate(winner_count = Count('winner')).order_by('-winner_count')[:1]
    # print(match)
    return list(match)

def location(year):
    match = Matches.objects.filter(season = year).values('winner').order_by().annotate(winner_count = Count('winner')).order_by('-winner_count')[:1].get()
    team = match['winner']
    match1 = Matches.objects.filter(season = year, winner = team).values('city').order_by().annotate(loc_count = Count('city')).order_by('-loc_count')[:1]
    # print(match1)
    return list(match1)

def per_bat(year):
    match = Matches.objects.filter(season = year, toss_decision = 'bat').values('toss_decision').count()
    match1 = Matches.objects.filter(season = year, toss_decision = 'field').values('toss_decision').count()
    bat_per = (match)*100/(match+match1)
    # print(match)
    # print(match1)
    # print(match+match1)
    return bat_per
    
def margin(year):
    match = Matches.objects.filter(season = year).values('win_by_runs','winner').order_by('-win_by_runs')[:1]
    # print(match)
    return list(match)
 
def number(year):
    match = Matches.objects.filter(season = year).values('win_by_wickets','winner').order_by('-win_by_wickets')[:5]
    # print(match)
    return list(match)
 
def toss_match(year):
    match = Matches.objects.filter(season = year).values('toss_winner','winner').filter(toss_winner = F('winner')).count()
    # print(match)
    return match
 