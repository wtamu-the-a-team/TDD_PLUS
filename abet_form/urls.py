from django.conf.urls import url, include
from abet_form import views, views_crud

urlpatterns = [
    url(r'^$', views.home_page, name='index'),
    url(r'^(?P<application_id>[0-9]+)/$', views.test, name='detail'),
    url(r'test_routing', views_crud.test_routing, name='results'),
    url(r'test_post', views_crud.test_post, name='results'),
    url(r'form_submit', views_crud.form_submit, name='form_submit'),
    url(r'^([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/get_application', views_crud.get_application, name='get_application')
]

