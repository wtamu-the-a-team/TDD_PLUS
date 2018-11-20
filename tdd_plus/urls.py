from django.conf.urls import include, url
from abet_form import views as abet_form_views
from abet_form import urls as abet_form_urls

urlpatterns = [
    url(r'^$', abet_form_views.home_page, name='home'),
    url(r'^abet_form/', include(abet_form_urls)),
]
