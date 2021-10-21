from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _


def generate_unique_slug(obj, Model, slug_source):
    base_slug = slugify(slug_source)
    slug = base_slug
    if not obj.id and Model.objects.filter(slug=slug).exists():
        n = 1
        slug = "{}-{}".format(base_slug, n)
        while Model.objects.filter(slug=slug).exists():
            n += 1
            slug = "{}-{}".format(base_slug, n)
    if obj.id and Model.objects.filter(slug=slug).exclude(id=obj.id).exists():
        n = 1
        slug = "{}-{}".format(base_slug, n)
        while Model.objects.filter(slug=slug).exclude(id=obj.id).exists():
            n += 1
            slug = "{}-{}".format(base_slug, n)

    return slug
