from django.db import models
from django.utils.translation import gettext as _
from wagtail.core.fields import StreamField

from core.company.blocks.header import HeadingBlock
from core.core.models import CommonInfo

from model_admin.hooks.buttons.handlers import FieldHandler


class Company(CommonInfo):
    trade_name = models.CharField(_("Razão Social"), max_length=255)

    TO_DUPLICATE = [
        FieldHandler("trade_name", prefix="COÉ ", suffix="______TESTE"),
    ]

    def __str__(self):
        return self.trade_name
