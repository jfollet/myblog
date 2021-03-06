from django.contrib.auth import logout
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext, loader

from myapp.models import Post
from .forms import NameForm, ContactForm

def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)

    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404

    context = {'post': post}
    return render(request, 'detail.html', context)


def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    template = loader.get_template('list.html')
    context = RequestContext(request, {'posts': posts})
    body = template.render(context)
    return HttpResponse(body, content_type="text/html")

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            your_name = form.cleaned_data['your_name']
            context = {'your_name': your_name}
            template = loader.get_template('thanks.html')
            return HttpResponse(template.render(context), content_type="text/html")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

def get_contact(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            template = loader.get_template('thanks.html')
            return HttpResponse(template.render(), content_type="text/html")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')