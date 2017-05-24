from django.conf.urls import url
from myapp.views import list_view

urlpatterns = [
    url(r'^$', list_view, name="blog_index"),
]