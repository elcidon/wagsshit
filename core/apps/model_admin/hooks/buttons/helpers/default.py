from .base import BaseButtonHelper
from ..components import DeleteButton, EditButton, InspectButton, DuplicateButton, AddButton


class DefaultButtonHelper(BaseButtonHelper):

    _buttons = [
        EditButton,
        DeleteButton,
        InspectButton,
        DuplicateButton,
    ]
