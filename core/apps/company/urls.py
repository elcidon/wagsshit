from django.template.response import TemplateResponse
from django.urls import path
from django.views.generic.base import TemplateResponseMixin, ContextMixin, View
from wagtail.admin.views.generic import HookResponseMixin

def unpublish(request):
    print('BLA')

app_name = 'company'

urlpatterns = [
    path('duplicate/', unpublish, name='duplicate'),
]

