from wagtail.contrib.modeladmin.options import (
    modeladmin_register
)
from django.utils.translation import gettext as _

from .models import Company
from ..core.hooks.buttons.helpers.default import DefaultButtonHelper
from ..core.hooks.modeladmin.options import HeroModelAdmin


@modeladmin_register
class CompanyAdmin(HeroModelAdmin):
    model = Company
    menu_label = _("Company")
    menu_icon = 'pilcrow'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('id', 'trade_name', 'created_at',)
    list_filter = ('trade_name',)
    search_fields = ('trade_name', )