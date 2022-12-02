from model_admin.hooks.buttons.helpers import BaseButtonHelper
from model_admin.hooks.buttons.components import DeleteButton, EditButton, InspectButton


class DefaultButtonHelper(BaseButtonHelper):

    buttons = [
        EditButton,
        DeleteButton,
        InspectButton,
    ]
