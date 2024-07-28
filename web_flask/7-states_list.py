#!/usr/bin/python3
"""
starts a Flask web application
"""


from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states_list')
def state_list():
    """
    route to a template displaying a list of states
    """
    states = storage.all('State')
    states = sorted(states.values(), key=lambda state: state.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_sql_session(exception):
    """
    Closes SQLAlchemy Session
    """
    storage.close()


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
