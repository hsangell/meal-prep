
from middleware import testy, index, user_profile
from flask import jsonify

def initialise_routes(app):
    if app:
        app.add_url_rule('/api/hallo', 'index', index)  # endpoint url, function name, function
        app.add_url_rule('/api/testy/', 'testy', testy)
        app.add_url_rule('/', 'list_routes', list_routes, methods=['GET'], defaults={'app':app})
        app.add_url_rule('/api/profile/<id>/', 'user_profile', user_profile)
        app.add_url_rule('/api/meal/', 'meal', meal)
    return None

def list_routes(app):
    routes = []
    for route in app.url_map.iter_rules():
        routes.append( {'Route': str(route),
                        'Endpoint': route.endpoint,
                        'Methods': list(route.methods)
                        })
    return jsonify({"Routes":routes, "Total":len(routes)})