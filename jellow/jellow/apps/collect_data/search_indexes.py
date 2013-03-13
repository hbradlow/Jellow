import datetime
from haystack import indexes
from collect_data.models import *


class ParagraphIndex(indexes.SearchIndex, indexes.Indexable):
    text= indexes.CharField(document=True, use_template=True, boost=1.0)
    tags= indexes.MultiValueField(boost=2.5)
    def prepare_tags(self,object):
        return [tag.tag for tag in object.tags.all()]
    def get_model(self):
        return Paragraph
    def index_queryset(self):
        return self.get_model().objects
    def load_all_queryset(self):
        # Pull all objects related to the Paragraph in search results.
        return Paragraph.objects.all().select_related()
