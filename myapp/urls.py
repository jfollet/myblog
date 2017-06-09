from django.conf.urls import url
from django.views.generic import TemplateView

from myapp.views import list_view, detail_view, get_name, get_contact, logout_page

urlpatterns = [
    url(r'^posts/(?P<post_id>\d+)/$', detail_view, name="blog_detail"),
    url(r'^$', list_view, name="blog_index"),
    url(r'^your-name/', get_name, name="blog_form"),
    url(r'^your-contact/', get_contact, name="blog_form2"),
    url(r'^accounts/logout/', logout_page, name="logout"),
]
