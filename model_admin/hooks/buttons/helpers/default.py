from .base import BaseButtonHelper
from ..components import DeleteButton, EditButton, InspectButton


class DefaultButtonHelper(BaseButtonHelper):

    buttons = [
        EditButton,
        DeleteButton,
        InspectButton,
    ]
