from pyramid.view import view_config


@view_config(route_name='home', renderer='react_pyramid:templates/index.html')
def my_view(request):
    return dict()