import uuid
from enum import Enum
import string

from django.db import models, IntegrityError
from django.utils.crypto import get_random_string


class SNType(Enum):
    TEAM = 0
    MEMBER = 1
    MOTION = 2


SN_TYPE_CHOICES = [(t.value, t.name) for t in SNType]


class SNPool(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sn = models.CharField(max_length=16, unique=True, editable=False)
    random_string = models.CharField(max_length=13, unique=True, editable=False)
    type = models.IntegerField(choices=SN_TYPE_CHOICES)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'cms_sn_pool'

    def generate_team_sn(self, save=True):
        return self._generate_sn(SNType.TEAM, save)

    def generate_member_sn(self, save=True):
        return self._generate_sn(SNType.MEMBER, save)

    def generate_motion_sn(self, save=True):
        return self._generate_sn(SNType.MOTION, save)

    def _generate_sn(self, sn_type: SNType, save=True):

        random_string = get_random_string(13, allowed_chars=string.digits)
        sumcheck = _calculate_sumcheck(random_string, sn_type.value)
        sn = f'1{sn_type.value}{random_string}{sumcheck}'
        self.sn = sn
        self.random_string = random_string
        self.type = sn_type.value
        if save:
            try:
                return self.save()
            except IntegrityError:
                return self._generate_sn(sn_type, save)
        else:
            return self

    @staticmethod
    def is_valid_sn(sn: str, sn_type: SNType):

        def _split_sn(_sn):
            _t = _sn[1]
            _random_string = _sn[2:-1]
            _sumcheck = _sn[-1]
            return {
                'sn_type': int(_t),
                'random_string': _random_string,
                'sumcheck': int(_sumcheck),
            }

        sn_data = _split_sn(sn)
        if sn_type.value != sn_data['sn_type']:
            return False
        sumcheck = _calculate_sumcheck(sn_data['random_string'], sn_data['sn_type'])
        return sumcheck == sn_data['sumcheck']


def _calculate_sumcheck(s: str, t: int):
    flag = True
    n_list = map(int, s)
    sum = t
    for d in n_list:
        if flag:
            sum += d * 2
        else:
            sum += d * 3
        flag = not flag
    return sum % 10
