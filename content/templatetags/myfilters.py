from django import template

register = template.Library()


@register.filter
def filter_by_date(queryset, post_time):
    return queryset.filter(date_field=post_time)
