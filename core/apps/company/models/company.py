from django.db import models
from django.utils.translation import gettext as _
from wagtail.core.fields import StreamField

from apps.company.blocks.header import HeadingBlock
from core.models import CommonInfo

from model_admin.hooks.buttons.handlers.base import FieldHandler


class Company(CommonInfo):
    trade_name = models.CharField(_("Razão Social"), max_length=255)

    HANDLER_FIELDS_TO_DUPLICATE = [
        FieldHandler("trade_name", prefix="CÓPIA______", suffix="______TESTE"),
    ]

    body = StreamField([
        ('heading', HeadingBlock()),
    ], default=None)

    def __str__(self):
        return self.trade_name
