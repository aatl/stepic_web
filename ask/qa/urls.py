from django.conf.urls import url, include, patterns
from qa.views import test

urlpatterns = patterns('qa.views',

    url(r'^$', test, name='home'),
#     url(r'^login/$', test, name='loginName'),
#     url(r'^signup/', test, name='signupName'),
# #  url(r'^question/(?P<123>)/$', test, name='questionName').
#     url(r'^ask/$', test, name='askName'),
#     url(r'^popular/$', test, name='popularName'),
#     url(r'^new/$', test, name='newName'),
)