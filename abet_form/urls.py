import uuid

from django.conf.urls import url, include
from abet_form import views, views_crud
from abet_form.models import User

urlpatterns = [
    # Support
    url(r'^$', views.home_page, name='index'),
    url(r'^(?P<application_id>[0-9]+)/$', views.test, name='detail'),
    url(r'test_routing', views_crud.test_routing, name='results'),
    url(r'test_simple_url_post', views_crud.test_simple_url_post, name='test_simple_url_post'),

    # CRUD Support
    url(r'^([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/view_user_applications',
        views_crud.view_user_applications, name='view_user_applications'),
    url(r'form_submit', views_crud.form_submit, name='form_submit'),
    url(r'update_application', views_crud.update_application, name='update_application'),
    url(r'^([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/add_application', views_crud.add_application,
        name='add_application'),
    url(r'^([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/remove_application',
        views_crud.remove_application, name='remove_application'),
    url(r'^([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/get_application',
        views_crud.get_application, name='get_application'),

    # JSON Support
    url(r'^([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/get_application_json',
        views_crud.get_application_json, name='get_application_json'),
]


def one_time_startup():
    if User.objects.all().count() is 0:
        print("No Users currently exist...creating one now")
        user = User(uuid_id=uuid.uuid4())
        user.save()
        print("User UUID -> %s" % user.uuid_id)
    else:
        print("User UUID -> %s" % User.objects.all().first().uuid_id)


one_time_startup()
