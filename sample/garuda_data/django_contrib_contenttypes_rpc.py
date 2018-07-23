# DO NOT EDIT THIS FILE MANUALLY
# THIS FILE IS AUTO-GENERATED
# MANUAL CHANGES WILL BE DISCARDED
# PLEASE READ GARUDA DOCS
from garuda.django.contrib.contenttypes.models import ContentType  # NOQA
GARUDA_IGNORE_FIELDS = ['created_on', 'updated_on', 'id']  # NOQA


def read_contenttype(*args, **kwargs):
    try:
        return ContentType.objects.get(*args, **kwargs)
    except ContentType.DoesNotExist:
        return None


def read_contenttypes_filter(*args, **kwargs):
    return ContentType.objects.filter(*args, **kwargs)


def create_contenttype(*args, **kwargs):
    for ignore_field in GARUDA_IGNORE_FIELDS:
        if ignore_field in kwargs:
            del kwargs[ignore_field]
    for key in list(kwargs):
        if kwargs[key] in [None, 'None', '']:
            del kwargs[key]
    return ContentType.objects.create(*args, **kwargs)


def update_contenttype(id, *args, **kwargs):
    for ignore_field in GARUDA_IGNORE_FIELDS:
        if ignore_field in kwargs:
            del kwargs[ignore_field]
    for key in list(kwargs):
        if kwargs[key] in [None, 'None', '']:
            del kwargs[key]
    return ContentType.objects.filter(id=id).update(*args, **kwargs)


def delete_contenttype(id):
    return ContentType.objects.get(id=id).delete()