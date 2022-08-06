'''Creating a python web service app'''


from flask import Flask
from routes import initialise_routes

# Create a Flask object (micro web service framework) with name of module.
app = Flask(__name__)

# @app.route('/') # alternative way to app.add_url_rule method (now located in routes/middleware

initialise_routes(app)

if __name__ == "__main__":
    app.run(debug=True)