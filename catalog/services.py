from catalog.models import Category
from config.settings import CACHE_ENABLE
from django.core.cache import cache


def get_category_from_cache():
    if not CACHE_ENABLE:
        return Category.objects.all()
    key = "category_list"
    categories = cache.get(key)
    if categories is not None:
        return categories
    categories = Category.objects.all()
    cache.set(key, categories)
    return categories
