"""
messcover URL Configuration
"""
from django.conf.urls import url
from messcover.views import IndexView, TreeView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='start_crawl'),
    url(r'^tree/', TreeView.as_view(), name='tree'),
]
