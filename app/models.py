from django.db import models

from . import generate_unique_slug


class Tag(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Content(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    slug = models.SlugField(max_length=255, blank=True, null=True, help_text='leave this field empty to auto-generate')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, Content, self.title)

        super(Content, self).save(*args, **kwargs)
