from django.conf.urls import url, include

from myapp.views import list_view, detail_view, get_name, get_contact

urlpatterns = [
    url(r'^posts/(?P<post_id>\d+)/$', detail_view, name="blog_detail"),
    url(r'^$', list_view, name="blog_index"),
    url(r'^your-name/', get_name, name="blog_form"),
    url(r'^your-contact/', get_contact, name="blog_form2"),
]
