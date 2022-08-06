from django import template

from news.models import Category, News

register = template.Library()

@register.simple_tag( name = 'get_list_categories' )
def get_categories():
    return Category.objects.all()

@register.simple_tag( name = 'get_list_news' )
def get_news():
    return News.objects.all()