import datetime
from haystack import indexes
from collect_data.models import *


class ParagraphIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    def get_model(self):
        return Paragraph
    def index_queryset(self):
        return self.get_model().objects
