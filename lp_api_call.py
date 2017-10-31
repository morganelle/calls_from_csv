"""Prototype to make api calls using data from an external file."""


import json

# Global vars, replace with env vars
CLIENT_KEY = ''
APP_ID = ''
API_VERSION = ''
URL = 'http://fake.com/api'
ACTION = 'setUserAttribute'


def build_params(data_params, lines):
    """Build a json object from a csv line."""
    lines_list = lines.split(',')
    if len(lines_list) > len(data_params):
        raise IndexError('Too many values', lines)
    data_updates = {}
    for i, param in enumerate(data_params):
        if lines_list[i].strip():
            data_updates[param] = lines_list[i].strip()
    return json.dumps(data_updates)


def build_api_link(line):
    """Build the api link to send."""
    return '{}?appId={}&clientKey={}&apiVersion={}&action={}&{}'.format(URL, APP_ID, CLIENT_KEY, API_VERSION, ACTION, build_params(line))


def api_call(filename):
    """."""
