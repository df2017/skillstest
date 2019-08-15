from django.template import  Library

register = Library()

def tostring(value):
    return str(value)

register.filter('tostring',tostring)