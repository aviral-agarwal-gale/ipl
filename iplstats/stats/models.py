from django.db import models


class Matches(models.Model):
    """This table consists of individual account per client."""
    season = models.IntegerField()
    city = models.CharField(max_length=100, null=True)
    date = models.DateTimeField(max_length=100, null=True)
    team1 = models.CharField(max_length=100, null=True)
    team2 = models.CharField(max_length=100, null=True)
    toss_winner = models.CharField(max_length=100, null=True)
    toss_decision = models.CharField(max_length=100, null=True)
    result = models.CharField(max_length=100, null=True)
    dl_applied = models.BooleanField()
    winner = models.CharField(max_length=100, null=True)
    win_by_runs = models.IntegerField()
    win_by_wickets = models.IntegerField()
    player_of_match = models.CharField(max_length=100, null=True)
    venue = models.CharField(max_length=100, null=True)
    umpire1 = models.CharField(max_length=100, null=True)
    umpire2 = models.CharField(max_length=100, null=True)
    umpire3 = models.CharField(max_length=100, null=True)

    # def __str__(self):
    #     return self.name


class Deliveries(models.Model):
    """These are the brands listed under an account."""
    match_id = models.ForeignKey(Matches, null=True, on_delete=models.SET_NULL)
    inning = models.IntegerField()
    batting_team = models.CharField(max_length=100, null=True)
    bowling_team = models.CharField(max_length=100, null=True)
    over = models.IntegerField()
    ball = models.IntegerField()
    batsman = models.CharField(max_length=100, null=True)
    non_striker = models.CharField(max_length=100, null=True)
    bowler = models.CharField(max_length=100, null=True)
    is_super_over = models.BooleanField()
    wide_runs = models.IntegerField()
    bye_runs = models.IntegerField()
    legbye_runs = models.IntegerField()
    noball_runs = models.IntegerField()
    penalty_runs = models.IntegerField()
    batsman_runs = models.IntegerField()
    extra_runs = models.IntegerField()
    total_runs = models.IntegerField()
    player_dismissed = models.CharField(max_length=100, null=True)
    dismissal_kind = models.CharField(max_length=100, null=True)
    fielder = models.CharField(max_length=100, null=True)

class Native(models.Model):
    DATE = models.DateTimeField(max_length=300, null=True)
    PCC_SITENAME = models.CharField(max_length=300, null=True)
    PCC_AUDIENCE = models.CharField(max_length=300, null=True)
    PCC_UNIT_TYPE = models.CharField(max_length=300, null=True)
    PCC_PLATFORM_DEVICE = models.CharField(max_length=300, null=True)
    CREATIVE_NAME = models.CharField(max_length=300, null=True)
    CREATIVE_TYPE = models.CharField(max_length=300, null=True)
    CREATIVE_PLACEMENT = models.CharField(max_length=300, null=True)
    CAMPAIGN_GROUP = models.CharField(max_length=300, null=True)
    HEADLINE = models.CharField(max_length=300, null=True)
    BODY = models.CharField(max_length=300, null=True)
    COST = models.FloatField(null=True)
    CLICKS = models.IntegerField(null=True)
    IMPRESSIONS = models.IntegerField(null=True)
    ENGAGEMENTS = models.IntegerField(null=True)
    LIKES = models.IntegerField(null=True)
    SHARES = models.IntegerField(null=True)
    LEADS = models.IntegerField(null=True)
    FOLLOWS = models.IntegerField(null=True)
    COMMENTS = models.IntegerField(null=True)
    REACTIONS = models.IntegerField(null=True)
    LANDING_PAGE_CLICKS = models.IntegerField(null=True)
