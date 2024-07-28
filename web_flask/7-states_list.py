#!/usr/bin/python3
"""
starts a Flask web application
"""


from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """
    route to a template displaying a list of states
    """
    states = storage.all(State)
    states = sorted(states.values(), key=lambda state: state.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_sql_session(arg=None):
    """
    Closes SQLAlchemy Session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
