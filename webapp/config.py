import json

with open('/etc/config.json') as config_file:
    config = json.load(config_file)

class Config(object):
    # Flask settings
    SECRET_KEY = config.get('SECRET_KEY')

    # Flask-SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False    # Avids SQLAlchemy warning
