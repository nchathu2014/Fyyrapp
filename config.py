import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = False

# Connect to the database
SQLALCHEMY_TRACK_MODIFICATIONS = False

# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgres://Froggie@127.0.0.1:5432/fyyrapp'