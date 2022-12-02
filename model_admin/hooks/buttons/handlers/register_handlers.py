import abc
from abc import ABC
from typing import Type, List
from django.db.models import Model

from model_admin.hooks.buttons.handlers.field_handler import FieldHandler, IFieldHandler


class IHandlers(ABC):
    """A class to handle any field registered

    Args:
        obj (Model): A django model, where we need to extract the field
        fields (List[IFieldHandler]): A list of all fields to be handle
        auto_import_unique_fields (bool): If is True, import all unique fields from model object
    """

    @abc.abstractmethod
    def __init__(self,
                 obj: Type[Model],
                 fields: List[IFieldHandler],
                 auto_import_unique_fields: bool = False):
        pass

    def handle(self):
        raise NotImplementedError()


class RegisterHandlers(IHandlers):
    """
    Implementation example:

    TO_DUPLICATE = RegisterHandlers(
        obj=self,
        fields=[
            FieldHandler("title"),
            SlugFieldHandler("slug"),
            FieldHandler("subtitle", prefix="CÓPIA", suffix="Anyshit")
        ],
        auto_import_unique_fields=True
    )
    """

    def __init__(self,
                 obj: Model,
                 auto_import_unique_fields: bool = True):
        self.obj = obj
        self.auto_import_unique_fields = auto_import_unique_fields

    def _import_unique_fields(self) -> List[IFieldHandler]:
        """Auto retrieve all unique fields defined in model

        Returns:
            List[str]: A list with all fields to modify
        """
        fields = []
        for field in self.obj._meta.get_fields():  # noqa
            if hasattr(field, "unique") and field.unique:
                if "id" not in field.name:
                    f = FieldHandler(field.name)
                    fields.append(f)
        return fields

    def _get_fields(self) -> List[IFieldHandler]:
        """Get all fields to concatenate the text COPY.

        Args:
            obj (Model): A Django model

        Returns
        """
        fields = self._import_unique_fields() if self.auto_import_unique_fields else []

        if hasattr(self.obj, "TO_DUPLICATE"):
            register_handlers = getattr(self.obj, "TO_DUPLICATE")
            fields = fields + register_handlers
        return fields

    @staticmethod
    def _duplicate(obj):
        obj.pk = None
        obj.save()
        return obj

    def handle(self) -> Model:
        obj = self.obj
        for field in self._get_fields():
            setattr(obj, field.name, field.handle(obj))
        return self._duplicate(obj)


