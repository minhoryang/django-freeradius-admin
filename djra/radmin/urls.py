from django.conf.urls.defaults import *

urlpatterns = patterns('djra.radmin.views',
    url(r'^$', 'home'), 
    url(r'^users/$', 'users'), 
    url(r'^users/create/$', 'create_user'), 
    url(r'^user/(?P<username>[^/]+)/$', 'user_detail'), 
    url(r'^user/(?P<username>[^/]+)/sessions/$', 'user_sessions'), 
    url(r'^groups/$', 'groups'), 
    url(r'^groups/create/$', 'create_group'), 
    url(r'^group/(?P<groupname>[\w\-]+)/$', 'group_detail'), 
)
