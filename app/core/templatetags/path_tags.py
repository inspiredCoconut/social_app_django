from django import template

register = template.Library()

@register.simple_tag(name='get_active_path_by_url_name')
def get_active_path_by_url_name(url_name, request):
    if request.resolver_match.url_name == url_name:
        return 'active'
    return ''