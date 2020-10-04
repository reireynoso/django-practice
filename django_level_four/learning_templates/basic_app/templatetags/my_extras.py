from django import template

# add to the library
register = template.Library()
@register.filter(name='cut')

def cut(value,arg):
    """
    cuts out all values of "arg" from the string
    """

    return value.replace(arg,"")

# takes in 2 params, name of the custom filter template and the function 
# register.filter('cut', cut)