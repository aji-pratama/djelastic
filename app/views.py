from django.shortcuts import render
from django.views.generic import ListView

from .documents import ContentDocument
from .models import Content


class HomeViews(ListView):
    template_name = 'home.html'
    model = Content
    context_object_name = 'contents'

    def get_queryset(self):
        qs = self.queryset

        search = self.request.GET.get('q', None)
        if search and len(search) > 0:
            qset = ContentDocument.search().query('multi_match', query=search)
            qs = qset.to_queryset()

        tag = self.request.GET.get('tag', '')
        if tag != '':
            qs = qs.filter(tags__name=tag)

        return qs
