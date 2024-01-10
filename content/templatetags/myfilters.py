from django import template

register = template.Library()


@register.filter
def custom_timesince(value):
    from django.utils.timesince import timesince

    if timesince(value).find("минут") != -1:
        return value.strftime("%S секунд назад")
    return timesince(value)
