from re import search
from typing import Type

from django.db.models import Model
from django.utils.text import slugify


class DuplicateObject:

    @classmethod
    def _set_copy_to_text(cls, obj: Type[Model], field: str) -> str:
        final_text = "COPY %s" % getattr(obj, field)
        if search("slug", field):
            final_text = slugify(final_text)
        return final_text

    @classmethod
    def do(cls, obj: Type[Model]):
        obj.pk = None
        if hasattr(obj, "UNIQUE_FIELDS_TO_DUPLICATE"):
            for field in obj.UNIQUE_FIELDS_TO_DUPLICATE:
                setattr(obj, field, cls._set_copy_to_text(obj, field))
        obj.save()


