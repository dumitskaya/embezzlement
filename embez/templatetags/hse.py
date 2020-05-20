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
    header = arg_dict.get('header')
    title = arg_dict.get('title')

    return CardNode(nodelist, header, title)


class CardNode(template.Node):
    def __init__(self, nodelist, header, title):
        self.nodelist = nodelist
        self.header = header
        self.title = title

    def render(self, context):
        output = self.nodelist.render(context)
        if self.header:
            header = self.header.resolve(context)
        else:
            header = None
        if self.title:
            title = self.title.resolve(context)
        else:
            title = None
        rendered = render_to_string('embez/tags/hse_card.html', {'content': output, "header": header,
                                                                 "title": title})
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
