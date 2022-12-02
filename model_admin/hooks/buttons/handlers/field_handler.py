import abc
from abc import ABC
from typing import Union
from django.db.models import Model


class IFieldHandler(ABC):
    """
    Base handler class

    Args:
        obj (Model): A django model, where we need to extract the field
        field (str): the field name that we want take the value
        prefix (str): the prefix that will be concatenated to the field. COPY is default
        suffix (str): a suffix that will be concatenated after the text of field. Empty is default
    """
    @abc.abstractmethod
    def __init__(self, *args, **kwargs) -> None:
        pass

    @abc.abstractmethod
    def _get_field_from_obj(self) -> str:
        pass

    @abc.abstractmethod
    def _concatenate_prefix_and_suffix_to_value(self) -> str:
        pass

    @abc.abstractmethod
    def _pre_handle(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def handle(self, obj: Model) -> str:
        raise NotImplementedError


class FieldHandler(IFieldHandler):

    def __init__(self, field, prefix="COPY ", suffix=""):
        self.obj = None
        self.name = field
        self.prefix = prefix
        self.suffix = suffix

    def _get_max_length(self) -> Union[int, None]:
        """Return text according to the max_length defined in Django field

        Args:
            obj (Model): A Django model
            field (str): The field name that will want to be found

        Returns:
            int: The maximum length of field
            None: If field has no maximum length
        """
        max_length = None
        field = self.obj._meta.get_field(self.name) # noqa
        if hasattr(field, "max_length"):
            max_length = field.max_length

        return max_length

    def _get_field_from_obj(self) -> str:
        field_value = getattr(self.obj, self.name)
        return field_value

    def _concatenate_prefix_and_suffix_to_value(self) -> str:
        formatted_text = "{prefix}{field_value}{suffix}".format(
            prefix=self.prefix,
            field_value=self._get_field_from_obj(),
            suffix=self.suffix
        )
        return formatted_text

    def _pre_handle(self) -> str:
        return self._concatenate_prefix_and_suffix_to_value()

    def handle(self, obj: Model) -> str:
        self.obj = obj
        return self._pre_handle()[0:self._get_max_length()]