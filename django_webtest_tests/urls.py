from django.conf.urls.defaults import *
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

def simple_method_test(request):
    return HttpResponse(unicode(request.method))

def simple_template_render(request, template_name):
    return render_to_response(template_name, {
        'foo': ('a', 'b', 'c'),
        'bar': True,
        'spam': None,
    }, context_instance=RequestContext(request))

urlpatterns = patterns('',
    url(r'^$', simple_method_test, name='simple-method-test'),
    url(r'^template/(.*)$', simple_template_render, name='simple-template-test'),
    url(r'^check-password/$', 'testapp_tests.views.check_password', name='check_password'),
    url(r'^search/$', 'testapp_tests.views.search', name='search')
)
