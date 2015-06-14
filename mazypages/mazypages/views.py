from django.views.generic.base import TemplateView
from mazypages import actions
from django.http import HttpResponseRedirect

from rest_framework import viewsets
from .serializers import RouteSerializer
from .models import Route


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        return context


class PeopleView(TemplateView):
    template_name = 'people.html'

    def get_context_data(self, **kwargs):
        context = super(PeopleView, self).get_context_data(**kwargs)
        context['users'] = actions.get_all_users()

        return context


class PlanView(TemplateView):
    template_name = 'plan.html'

    def get_context_data(self, **kwargs):
        context = super(PlanView, self).get_context_data(**kwargs)
        context['plan'] = actions.get_plan()

        return context


class RegView(TemplateView):
    template_name = 'sign_up.html'

    def get_context_data(self, **kwargs):
        context = super(RegView, self).get_context_data(**kwargs)

        return context


class LogView(TemplateView):
    template_name = 'sign_in.html'

    def get_context_data(self, **kwargs):
        context = super(LogView, self).get_context_data(**kwargs)

        return context


def red_page(request, id):
    return HttpResponseRedirect('/')


class RouteView(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
