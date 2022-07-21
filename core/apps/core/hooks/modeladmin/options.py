from django.urls import re_path
from wagtail.contrib.modeladmin.options import ModelAdmin

from apps.core.hooks.buttons.helpers.default import DefaultButtonHelper
from apps.core.hooks.views.duplicate import DuplicateView


class HeroModelAdmin(ModelAdmin):

    button_helper_class = DefaultButtonHelper
    duplicate_view_class = DuplicateView
    duplicate_template_name: str = ''

    def duplicate_view(self, request, instance_pk):
        kwargs = {'model_admin': self, 'instance_pk': instance_pk}
        view_class = self.duplicate_view_class
        return view_class.as_view(**kwargs)(request)

    def get_duplicate_template(self):
        return self.duplicate_template_name or self.get_templates('duplicate')

    def get_admin_urls_for_registration(self):
        urls = super().get_admin_urls_for_registration()
        urls = urls + (
            re_path(
                self.url_helper.get_action_url_pattern('duplicate'),
                self.duplicate_view,
                name=self.url_helper.get_action_url_name('duplicate')),
        )
        return urls
