from django import template

register = template.Library()


@register.filter()
def multiply(value, arg):
    return f'{float(value) * arg:.2f}'