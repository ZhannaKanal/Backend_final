from django import template
from posts.models import *
register=template.Library()

#--1
@register.simple_tag(name='getkalas')
def get_kalas():
    return Kala.objects.all()
#--2
@register.inclusion_tag('posts/list_price.html')
def show_kalas():
    kala=InfoTravel.objects.order_by('id')[:1]
    return{'kala':kala}
