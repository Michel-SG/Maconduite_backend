from flask import Flask
import flask_sqlalchemy
import os
import logging
from maconduite_back import loginconfig

logger = logging.getLogger(__name__)

db = flask_sqlalchemy.SQLAlchemy()

from maconduite_back.routes.auth import auth


def create_app():
    """
    This is the main function used to generate a Flask object with configuration parameters.

    Parameters:
        None

    Returns:
        flask.Flask: the Flask object which implements a WSGI application
        See also https://flask.palletsprojects.com/en/2.0.x/api/#flask.Flask
    """

    app = Flask(
        __name__, static_folder="../maconduite_frontend/build", static_url_path="/"
    )
    app.config.update(
        SQLALCHEMY_DATABASE_URI=(
            # 'sqlite:///'
            # + os.path.join(os.path.dirname(os.path.realpath(__file__)), 'debug.db')
            "postgresql://MICHEL:MICHELPOSTGRES@localhost:5432/MACONDUITE"
        ),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        # SECRET_KEY = JWT_SECRET,
        JWT_SECRET="\xe1\xd8\x5f\x3a\x53\x05\x7b\x66\x6d\xf8\x20\x9b\xb0\xb3\xa5\x4a",
        JWT_ALGORITHM="HS256",
        JWT_EXP_DELTA_HOURS=2,
        # UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)),'uploaded_files'),
        # ALLOWED_EXTENSIONS = {'DAT'},
        MAX_CONTENT_LENGTH=16 * 1024 * 1024,  # = 16 MB
        SQLALCHEMY_ECHO=False,
    )

    # initializing the flask_sqlalchemy object with the application context
    db.init_app(app)
    add_mock_data(app)

    app.register_blueprint(auth)

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    return app


def add_mock_data(app):
    """
    This function inserts mock data into database for testing :
        - 1 User

    It also clean the database from previous testing data to avoid conflicts.
    """
    # -------------------------------  TESTING DATA  ------------------------------------
    with app.app_context():
        from maconduite_back.models.user import User
        from datetime import datetime

        # logger.info('Initializing database with testing data.')
        logger.info("> Creating new tables.")
        db.create_all()
        db.session.commit()

        # user1 = User(email='admin', password="michel", first_name='SADEU', last_name='NGAKOU')
        # user2 = User(email='mick', password="michelo", first_name='SADEUH', last_name='NGAKOU')
        # db.session.add(user1)
        # db.session.add(user2)
        # db.session.commit()
        # print(user1.json_out())
        # print(user2.json_out())
        logger.info("Database has been successfully connected.")
