"""
mazypa URL Configuration
"""
from django.conf.urls import url, include
from mazypages import views

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'route', views.RouteView)


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='home'),
    url(r'^people/$', views.PeopleView.as_view(), name='people'),
    url(r'^plan/$', views.PlanView.as_view(), name='plan'),
    url(r'^login/$', views.LogView.as_view(), name='login'),
    url(r'^register/$', views.RegView.as_view(), name='register'),
    url(r'^user/(\d+)/$', views.red_page),
    url(r'^api/', include(router.urls)),
]
