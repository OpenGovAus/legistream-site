from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name='legistream-home'),
    path('federal/', views.federal, name='federal-parliament'),
    path('qld/', views.qld, name='qld-parliament'),
    path('wa/', views.wa, name='wa-parliament'),
    path('act/', views.act, name='act-parliament'),
    path('nsw/', views.nsw, name='nsw-parliament'),
    path('nt/', views.nt, name='nt-parliament'),
    path('vic/', views.vic, name='vic-parliament'),
    path('tas/', views.tas, name='tas-parliament'),
    path('sa/', views.sa, name='sa-parliament'),
    path('demoparl/', views.demoparl, name='demo-parliament'),
    path('info/', views.info, name='info-pg'),
    path('robots.txt', TemplateView.as_view(template_name='legistream/robots.txt', content_type='text/plain'))
]