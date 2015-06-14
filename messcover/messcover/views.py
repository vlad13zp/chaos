from django.views.generic.base import TemplateView
from messcover.actions import run_spider, get_main_urls
from messcover.actions import get_help_urls, clear_base


class TreeView(TemplateView):
    template_name = 'tree.html'

    def get_context_data(self, **kwargs):
        context = super(TreeView, self).get_context_data(**kwargs)

        context['main_urls'] = get_main_urls()
        context['help_urls'] = get_help_urls()

        return context


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        clear_base()
        run_spider()

        return context
