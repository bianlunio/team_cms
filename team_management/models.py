from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.functional import SimpleLazyObject
from rest_framework.authtoken.models import Token

from sn_dispatcher.tools import generate_team_sn, generate_member_sn


class Team(models.Model):
    sn = models.CharField(max_length=16, unique=True, default=generate_team_sn)
    name = models.CharField('队伍名称', max_length=100)
    created = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        db_table = 'cms_team'


class Member(models.Model):
    sn = models.CharField(max_length=16, unique=True, default=generate_member_sn)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member')
    name = models.CharField('姓名', max_length=10)
    nickname = models.CharField('昵称', max_length=10)
    school = models.CharField('学校', max_length=30)

    @property
    def team(self):
        def get_team(member):
            return member.teams.first().team
        return SimpleLazyObject(lambda: get_team(self))

    class Meta:
        db_table = 'cms_member'


class TeamMember(models.Model):
    team = models.ForeignKey(Team, related_name='members', on_delete=models.CASCADE)
    member = models.ForeignKey(Member, related_name='teams', on_delete=models.CASCADE)
    date_joined = models.DateTimeField('加入时间', auto_now_add=True)

    class Meta:
        db_table = 'cms_team_member'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
