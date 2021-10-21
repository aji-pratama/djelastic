from django.contrib import admin

from .models import Tag, Category, Content


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']


admin.site.register(Tag)
admin.site.register(Category)
