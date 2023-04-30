from django import template

register = template.Library()

@register.filter(name='lookup')
def get_item(dictionary, key):
    return dictionary.get(key)



