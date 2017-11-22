from django.db import models

from sn_dispatcher.tools import generate_motion_sn


class Motion(models.Model):
    sn = models.CharField(max_length=16, unique=True, default=generate_motion_sn)
    title = models.CharField('辩题名称', max_length=100)
    title_zheng = models.CharField('正方持方', max_length=100)
    title_fan = models.CharField('反方持方', max_length=100)
    description = models.TextField('题解')
    comment = models.TextField('备注')
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cms_motion'


class TeamMotion(models.Model):
    team = models.ForeignKey('team_management.Team', related_name='motions', on_delete=models.CASCADE)
    motion = models.ForeignKey(Motion, related_name='teams', on_delete=models.CASCADE)

    class Meta:
        db_table = 'cms_team_motion'
