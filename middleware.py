from flask import jsonify, request, abort

meals = ["carbonara", "veal ragu", "fish and chips"]

def index():
    return "Hallo World"

# @app.route('/api/testy')
def testy():
    return "Hello testing"

def user_profile(id):
    return f"Profile page of user #{id}"

def meal():
    return jsonify(meals)