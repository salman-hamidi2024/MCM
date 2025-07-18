from django import template  

register = template.Library()  

@register.filter  
def add_class(field, css_class):  
    """ Adds a CSS class to a form field. """  
    field.field.widget.attrs['class'] = css_class  
    return field
@register.filter
def add_type(field, type):
    field.field.widget.attrs["type"] = type
    return field