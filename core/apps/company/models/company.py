from django.db import models
from django.utils.translation import gettext as _
from wagtail.core.fields import StreamField

from apps.company.blocks.header import HeadingBlock
from model_admin.models import CommonInfo


class Company(CommonInfo):
    # TODO: Apenas um todo pra testar no sonarcloud
    trade_name = models.CharField(_("Razão Social"), max_length=255)

    UNIQUE_FIELDS_TO_DUPLICATE = [
        "trade_name"
    ]

    body = StreamField([
        ('heading', HeadingBlock()),
    ], default=None)

    def __str__(self):
        return self.trade_name
