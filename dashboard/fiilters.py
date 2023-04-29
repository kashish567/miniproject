import django_filters
from . models import *
class AnsFilter(django_filters.FilterSet):

    class Meta:
        model = Questions
        fields = ['qDiffLvl']