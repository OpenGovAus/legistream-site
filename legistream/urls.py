from django.urls import path
from . import views
from django.views.generic import TemplateView
from . import module_list


'''
Since the backend uses the same model for every parliament, we can safely
and dynamically generate the URLs for them using inspect().
'''

urlpatterns = [
    path('', views.home, name='legistream-home'),
    path('info/', views.info, name='info-pg'),
    path('robots.txt', TemplateView.as_view(
        template_name='legistream/robots.txt', content_type='text/plain'))
]


for mod in module_list:
    exec(f'urlpatterns.append(path("{mod}/", views.watch, '
         f'name="{mod}-parliament"))', globals(), locals())
