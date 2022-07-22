from wagtail.contrib.modeladmin.options import (
    modeladmin_register
)
from django.utils.translation import gettext as _

from .models import AcidBath
from ..model_admin.hooks.modeladmin.options import HeroModelAdmin


@modeladmin_register
class AcidBathAdmin(HeroModelAdmin):
    model = AcidBath
    menu_label = _("Acid Bath")
    menu_icon = 'pilcrow'
    menu_order = 190
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('id', 'title', 'created_at',)
    list_filter = ('title',)
    search_fields = ('title', )
