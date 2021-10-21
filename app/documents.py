from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from .models import Content


@registry.register_document
class ContentDocument(Document):

    class Index:
        name = 'contents'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    class Django:
        model = Content
        fields = [
            'title',
            'body',
        ]
