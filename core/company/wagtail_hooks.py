from wagtail.contrib.modeladmin.options import (
    modeladmin_register
)
from django.utils.translation import gettext as _

from .models import Company
from model_admin.hooks.buttons.components import DuplicateButton
from model_admin.hooks.modeladmin import BaseModelAdmin


@modeladmin_register
class CompanyAdmin(BaseModelAdmin):
    model = Company
    menu_label = _("Company")
    menu_icon = 'pilcrow'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('id', 'trade_name', 'created_at',)
    list_filter = ('trade_name',)
    search_fields = ('trade_name', )

    add_custom_buttons = [
        DuplicateButton,
    ]
