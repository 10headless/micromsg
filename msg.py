import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, jsonify
import sqlite3

app = Flask(__name__)

app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
    DATABASE = 'msg.db'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

from views import *

if __name__ == "__main__":
    app.run()