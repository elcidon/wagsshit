from django.utils.text import slugify

from model_admin.hooks.buttons.handlers.field_handler import FieldHandler


class SlugFieldHandler(FieldHandler):
    def _pre_handle(self):
        result_text = super()._pre_handle()
        return slugify(result_text)
