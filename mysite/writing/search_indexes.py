import datetime

from haystack import indexes

from writing.models import Document


class DocumentIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    user = indexes.CharField(model_attr='writer.user')
    created = indexes.CharField(model_attr='created')
    modified = indexes.CharField(model_attr='modified')

    def get_model(self):
        return Document

    def index_queryset(self, using=None):
        """
        Used when the entire index for model is updated.

        :param using:
        :return:
        """
        return self.get_model().objects.filter(modified__lte=datetime.datetime.now())