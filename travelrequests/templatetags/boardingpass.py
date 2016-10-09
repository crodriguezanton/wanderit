
from django.template import Node, Library, TemplateSyntaxError
from django.utils import six

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
        #with context.push(student):
        #    return self.nodelist.render(context)

@register.tag('boardingpass')
def do_with(parser, token, *args):
    """
    Adds one or more values to the context (inside of this block) for caching
    and easy access.
    For example::
        {% with total=person.some_sql_method %}
            {{ total }} object{{ total|pluralize }}
        {% endwith %}
    Multiple values can be added to the context::
        {% with foo=1 bar=2 %}
            ...
        {% endwith %}
    The legacy format of ``{% with person.some_sql_method as total %}`` is
    still accepted.
    """
    bits = token.split_contents()
    remaining_bits = bits[1:]
    extra_context = {
        'report': bits[1],
    }
    nodelist = parser.parse(('endboardingpass',))
    parser.delete_first_token()
    return WithNode(None, None, nodelist, extra_context=extra_context)