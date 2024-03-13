import os
import pytest


from maconduite_back.app import create_app
from maconduite_back.models.user import User
from maconduite_back.app import db as database


@pytest.fixture
def app():
    """
    Fixture providing the Flask application.

    Note that we never require this fixture directly !
    In our tests, we require the `client` fixture, which is provided by the pytest-flask
    framework, based on the `app` fixture.

    If we weren't using pytest-flask, we should implement ourselves the `client` fixture,
    which returns app.test_client().
    """
    app = create_app()
    with app.app_context():
        database.create_all()
        database.session.commit()
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def db():
    """
    Fixture providing a SQLite database.
    SQLite is a file-based database, so it's very useful for unit testing.
    (There is no data persistence).

    Note that we require the `client` fixture eventhough it is not used in this function.
    It's because the database fixture needs the app.app_context() object.
    In particular, the database needs the app context because the path to the file
    `database.db` is defined in app.config['SQLALCHEMY_DATABASE_URI'], i.e. inside the app,
    and not inside the db object.

    That's why the db fixture requires the `client` fixture.
    (We could instead require the `app` fixture, it makes no difference.)
    """
    # database.drop_all()
    # database.create_all()
    # database.session.commit()

    return database
