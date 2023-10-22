#!/usr/bin/python3
""" Script that runs a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """ Closes the session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Displays a html page that contains states and cities """
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
