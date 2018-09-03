from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^index/$', views.index, name='index'),
	url(r'^index/(?P<letter>[A-Z])$', views.alphabet_view, name='index'),
	url(r'detail(?P<pk>\d+)/$', views.detail, name='detail'),
	url(r'detail(?P<mineral_pk>\d+)/$', views.detail, name='detail'),
	url(r'search_results/$', views.search_results, name='search_results'),
	url(r'group_view/$', views.group_view, name='group_view'),
	url(r'group_view/<(?P<group>\w+)/$', views.group_view, name='group_view'),
	url(r'', views.route, name='route'),
]