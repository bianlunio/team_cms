from .models import SNPool


def generate_team_sn():
    pool = SNPool()
    pool.generate_team_sn()
    return pool.sn


def generate_member_sn():
    pool = SNPool()
    pool.generate_member_sn()
    return pool.sn


def generate_motion_sn():
    pool = SNPool()
    pool.generate_motion_sn()
    return pool.sn
