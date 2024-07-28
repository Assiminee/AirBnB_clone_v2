#!/usr/bin/python3
"""
starts a Flask web application
"""


from flask import Flask, render_template
from models import storage
app = Flask(__name__)
template_path = "10-hbnb_filters.html"


@app.route('/hbnb_filters')
def hbnb_filters():
    """
    route to a template displaying a filters
    """
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values
    return render_template(template_path, states=states, amenities=amenities)


@app.teardown_appcontext
def teardown_sql_session(exception):
    """
    Closes SQLAlchemy Session
    """
    storage.close()


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
