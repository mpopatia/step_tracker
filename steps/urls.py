from django.conf.urls import url
from steps import views


urlpatterns = [
    url('^$', views.index, name='index'),
]