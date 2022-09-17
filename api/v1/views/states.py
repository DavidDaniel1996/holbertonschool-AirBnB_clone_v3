#!/usr/bin/python3

from crypt import methods
from flask import Flask, request, jsonify, abort
from models import storage
from models.state import State
from api.v1.views import app_views


@app_views.route('/states', strict_slashes=False, methods=['GET'])
def all_states():
    state_objects = storage.all(State)
    states_list = []
    for key, val in state_objects.items():
        states_list.append(val.to_dict())
    return jsonify(states_list)


@app_views.route('/states/<state_id>', strict_slashes=False, methods=['GET'])
def state_by_id(state_id):
    state_objects = storage.all(State)
    for key, val in state_objects.items():
        if val.id == state_id:
            return val.to_dict()
    abort(404)
