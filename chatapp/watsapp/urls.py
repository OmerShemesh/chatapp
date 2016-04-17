from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^register/$', views.register,name='register'),
    url(r'^(?P<user_id>[0-9]+)/$', views.message, name='message'),


]
