from django.conf.urls import url, include
from abet_form import views, views_crud

urlpatterns = [
    url(r'^$', views.home_page, name='index'),
    url(r'^(?P<application_id>[0-9]+)/$', views.test, name='detail'),
    url(r'test_routing', views_crud.test_routing, name='results'),
    url(r'test_post', views_crud.test_post, name='results'),
    url(r'details', views_crud.details, name='details')
]

