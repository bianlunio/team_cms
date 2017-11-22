import random

from django.test import TestCase

from .models import SNPool, SNType


class SNPoolModelTests(TestCase):
    try_count = 1000

    def test_generate_sn(self):
        for i in range(self.try_count):
            sn_type = random.choice((SNType.TEAM, SNType.MEMBER, SNType.MOTION))
            pool = SNPool()
            if sn_type == SNType.TEAM:
                pool.generate_team_sn()
            elif sn_type == SNType.MEMBER:
                pool.generate_member_sn()
            else:
                pool.generate_motion_sn()
            self.assertTrue(pool.is_valid_sn(pool.sn, SNType(pool.type)))
