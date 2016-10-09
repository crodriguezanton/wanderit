from django.template import Node, Library

from searchreports.models import Report

register = Library()


class WithNode(Node):
    def __init__(self, var, name, nodelist, extra_context=None):
        self.nodelist = nodelist
        self.extra_context = extra_context or {}
        self.reportkey = extra_context['report']

    def __repr__(self):
        return "<WithNode>"

    def render(self, context):

        report = context[self.reportkey]
        assert isinstance(report, Report)

        context['carrier'] = report.get_carrier()
        context['recommendation'] = report.get_recommendation_html()
        context['price_trend'] = report.get_price_trend_html()
        context['pricing_option'] = report.get_pricing_option()

        return self.nodelist.render(context)


@register.tag('boardingpass')
def do_with(parser, token, *args):

    bits = token.split_contents()
    extra_context = {
        'report': bits[1],
    }
    nodelist = parser.parse(('endboardingpass',))
    parser.delete_first_token()
    return WithNode(None, None, nodelist, extra_context=extra_context)