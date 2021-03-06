from haystack import indexes
from .models import CarModel


class CarModelIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    price = indexes.IntegerField(model_attr='price')
    milage = indexes.IntegerField(model_attr='milage')
    content_auto = indexes.EdgeNgramField(model_attr='name')

    def get_model(self):
        return CarModel
