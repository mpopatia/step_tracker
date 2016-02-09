from django.conf.urls import url
from steps import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^store_steps/$', views.store_steps, name='store_steps'),
    url(r'^success/$', views.success, name='success'),
]