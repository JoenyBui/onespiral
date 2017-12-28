import datetime

from haystack import indexes

from django.contrib.auth.models import User
from core.models import Profile


class ProfileIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    first_name = indexes.CharField(model_attr='first_name')
    last_name = indexes.CharField(model_attr='last_name')
    email = indexes.CharField(model_attr='email')

    def get_model(self):
        return User
