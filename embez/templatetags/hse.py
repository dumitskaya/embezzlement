from django import template

from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django.template.loader import render_to_string
from django.template.base import token_kwargs

register = template.Library()
import re


@register.tag(name="card")
def do_card(parser, token, ):
    nodelist = parser.parse(('endcard',))
    parser.delete_first_token()
    bits = token.split_contents()
    tagname = bits.pop(0)
    arg_dict = token_kwargs(bits, parser)

    return CardNode(nodelist, **arg_dict)


class CardNode(template.Node):
    type_correspondence = dict(primary='text-white bg-primary',
                               secondary='text-white bg-secondary',
                               success='text-white bg-success',
                               danger='text-white bg-danger',
                               warning='text-white bg-warning ',
                               info='text-white bg-info ',
                               light='bg-light',
                               dark='bg-dark'
                               )

    def __init__(self, nodelist, **kwargs):
        self.nodelist = nodelist
        self.kwargs = kwargs

    def build_kwargs(self, context):
        registered_kwargs = dict(style=None, header=None, title=None)
        for k, v in registered_kwargs.items():
            current_k = self.kwargs.get(k)
            if current_k:
                registered_kwargs[k] = current_k.resolve(context)
        style = registered_kwargs['style']
        if self.type_correspondence.get(style):
            registered_kwargs['style'] = self.type_correspondence.get(style)

        return registered_kwargs

    def render(self, context):
        output = self.nodelist.render(context)
        kwargs = self.build_kwargs(context)
        rendered = render_to_string('embez/tags/hse_card.html', {'content': output, **kwargs})
        return rendered


@register.filter
def rubl(value):
    value = str(value)
    p = re.compile(r'^(?P<value>\d+)')
    m = p.search(value)
    re_val = m.group('value')
    if re_val:
        lasttwo = int(re_val[-2:]) if len(re_val) > 2 else int(re_val)
        lastdigit = int(re_val[-1])
        if 5 <= lasttwo <= 20:
            r = 'рублей'
        elif 2 <= lastdigit <= 4:
            r = 'рубля'
        elif lastdigit == 1:
            r = 'рубль'
        else:
            r = 'рублей'

        return re_val + " " + r
    return value


@register.inclusion_tag('embez/tags/hse_button.html', name='hse_button')
def next_button(label=_('Next'), html_class='btn-primary', *args, **kwargs):
    return dict(label=label, html_class=html_class)
