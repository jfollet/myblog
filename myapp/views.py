from django.template import RequestContext, loader
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

from myapp.models import Post


def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    template = loader.get_template('list.html')
    context = RequestContext(request, {'posts': posts})
    body = template.render(context)
    return HttpResponse(body, content_type="text/html")