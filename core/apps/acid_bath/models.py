from django.db import models
from django.utils.translation import gettext as _
from core.models import CommonInfo
from ckeditor.fields import RichTextField


class AcidBath(CommonInfo):
    title = models.CharField(_("Title"), max_length=255)
    content = RichTextField()
