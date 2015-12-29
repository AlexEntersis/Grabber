__author__ = 'Alex'

from haystack import indexes
from basic_parser.models import Profile, Skills


class ProfileIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr="name")
    title = indexes.CharField(model_attr="title")
    email = indexes.CharField(model_attr="email")
    phone = indexes.CharField(model_attr="phone")
    im = indexes.CharField(model_attr="im")
    url = indexes.CharField(model_attr="url")
    address = indexes.CharField(model_attr="address")
    advice_to_connect = indexes.CharField(model_attr="advice_to_connect")
    skills = indexes.MultiValueField(model_attr="skills", indexed=True, stored=True)

    def prepare_skills(self, obj):
        return [skills.id for skills in obj.skills.all()]

    def get_model(self):
        return Profile

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()


