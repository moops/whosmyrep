from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'whosmyrep.reps.views.index'),
	url(r'^(?P<rep_id>\d+)/$', 'whosmyrep.reps.views.detail'),
	url(r'^(?P<rep_id>\d+)/rank/$', 'whosmyrep.reps.views.rank'),
)