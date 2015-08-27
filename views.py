import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, jsonify
import sqlite3
import dbfunc
from msg import app



@app.route('/')
def index():
	return "whhhaaaat"
