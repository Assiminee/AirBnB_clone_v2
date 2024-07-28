#!/usr/bin/python3
"""
starts a Flask web application
"""


from flask import Flask, render_template
from models import storage
app = Flask(__name__)
template_path = "9-states.html"


@app.route('/states')
def state_list():
    """
    route to a template displaying a list of states
    """
    states = storage.all('State').values()
    return render_template(template_path, states=states)


@app.route('/states/<id>')
def state_by_id(id):
    """
    route to a template displaying the state with <id>
    and the cities in it
    """
    states = storage.all('State')
    for state in states.values():
        if state.id == id:
            return render_template(template_path, states=state)
    return render_template(template_path, states=None)

@app.teardown_appcontext
def teardown_sql_session(exception):
    """
    Closes SQLAlchemy Session
    """
    storage.close()


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
