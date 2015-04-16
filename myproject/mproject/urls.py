from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),    
    url(r'^$', "practica2.views.all"),
    url(r'^(.*)$', "practica2.views.info"), 
    #url(r'^(.*)$', "practica2.views.notfound")
)
