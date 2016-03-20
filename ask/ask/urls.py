from django.conf.urls import patterns, include, url
from qa.views import test, homeHandle,popularHandle, questionsHandler, askHandler, answerHandle

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', homeHandle, name='home'),
    url(r'^test/', test),
    url(r'^login/', 'qa.views.test', name='loginName'),
    url(r'^signup/', include('qa.urls')),
    url(r'^question/(?P<questionId>\d+)$', questionsHandler, name='questionReverse'),
    url(r'^ask/', askHandler, name='askName'),
    url(r'^popular/', popularHandle , name='popularName'),
    url(r'^new/$', include('qa.urls'), name='newName'),
    url(r'^answer', answerHandle )

)
