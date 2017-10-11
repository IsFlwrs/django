from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^base/$', views.BaseView.as_view(), name='base'),
    url(r'^template/$', views.HomeTemplateView.as_view(), name='templateView'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.PersonDetailView.as_view(), name='detail'),
    url(r'^list/$', views.PersonList.as_view(), name='list'),
    url(r'^create/$', views.PersonCreate.as_view(), name='create'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.PersonUpdate.as_view(), name='update'),
]