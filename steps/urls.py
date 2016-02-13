from django.conf.urls import url
from steps import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^store_steps/$', views.store_steps, name='store_steps'),
    url(r'^success/$', views.success, name='success'),
    url(r'^send_emails/$', views.send_emails, name='send_emails'),
    url(r'^increase_tester/$', views.increase_tester, name='increase_tester'),
    url(r'^get_tester/$', views.get_tester, name='get_tester'),
    url(r'^get_time/$', views.get_time, name='get_time'),
]