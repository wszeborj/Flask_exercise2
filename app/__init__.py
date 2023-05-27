from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from .constants import DB_PATH

db = SQLAlchemy()
ma = Marshmallow()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'

    db.init_app(app)
    ma.init_app(app)
    app.debug = True

    from .main_api import add_note_blueprint, get_notes_blueprint, \
        get_note_blueprint, update_note_blueprint, delete_note_blueprint

    app.register_blueprint(add_note_blueprint)
    app.register_blueprint(get_notes_blueprint)
    app.register_blueprint(get_note_blueprint)
    app.register_blueprint(update_note_blueprint)
    app.register_blueprint(delete_note_blueprint)

    return app
