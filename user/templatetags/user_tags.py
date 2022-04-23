from django import template

register = template.Library()

@register.filter(name='is_teacher')
def is_teacher(user):
    return user.groups.filter(name='teacher').exists()

@register.filter(name='is_student')
def is_student(user):
    return user.groups.filter(name='student').exists()
