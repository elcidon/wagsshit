from django.urls import path

def unpublish(request):
    print('BLA')

app_name = 'company'

urlpatterns = [
    path('duplicate/', unpublish, name='duplicate'),
]

