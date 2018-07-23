# DO NOT EDIT THIS FILE MANUALLY
# THIS FILE IS AUTO-GENERATED
# MANUAL CHANGES WILL BE DISCARDED
# PLEASE READ GARUDA DOCS
from garuda.sample.core.models import Article  # NOQA
GARUDA_IGNORE_FIELDS = ['created_on', 'updated_on', 'id']  # NOQA


def read_article(*args, **kwargs):
    try:
        return Article.objects.get(*args, **kwargs)
    except Article.DoesNotExist:
        return None


def read_articles_filter(*args, **kwargs):
    return Article.objects.filter(*args, **kwargs)


def create_article(*args, **kwargs):
    for ignore_field in GARUDA_IGNORE_FIELDS:
        if ignore_field in kwargs:
            del kwargs[ignore_field]
    for key in list(kwargs):
        if kwargs[key] in [None, 'None', '']:
            del kwargs[key]
    return Article.objects.create(*args, **kwargs)


def update_article(id, *args, **kwargs):
    for ignore_field in GARUDA_IGNORE_FIELDS:
        if ignore_field in kwargs:
            del kwargs[ignore_field]
    for key in list(kwargs):
        if kwargs[key] in [None, 'None', '']:
            del kwargs[key]
    return Article.objects.filter(id=id).update(*args, **kwargs)


def delete_article(id):
    return Article.objects.get(id=id).delete()