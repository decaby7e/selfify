#!/usr/bin/python3
from flask import Flask, request, redirect, send_from_directory, url_for
import yaml

import inspect  # Debugging

CONFIG_FILE = 'config.yaml'
SITE_FILE = 'sites.yaml'

## Variables ##

app = Flask(__name__)

config = {}
with open(CONFIG_FILE, 'r') as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as ex:
        print(ex)

sites = {}
with open(SITE_FILE, 'r') as stream:
    try:
        sites = yaml.safe_load(stream)
    except yaml.YAMLError as ex:
        print(ex)

## Routes ##

@app.route('/')
def home():
    return 'Hello world!'

@app.route('/<path>', subdomain="<subdomain>")
def site(path, subdomain):
    for site in sites:
        if sites[site]['subdomain'] == subdomain:
            return send_from_directory(f'../data/{site}', path)
    return 404

@app.route('/', subdomain="<subdomain>")
def site_root(subdomain):
    return app.send_static_file('index.html')

## Main ##

if __name__ == '__main__':
    app.config['SERVER_NAME'] = 'example.com:8080'
    app.run(debug=True)