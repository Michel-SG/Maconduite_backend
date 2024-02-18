from flask import Blueprint, request, jsonify, abort, Response, current_app
from http import HTTPStatus
import sqlalchemy
from maconduite_back.models.user import User

from maconduite_back.app import db, logger

# (1) We instanciate the blueprint
auth = Blueprint('auth', __name__)

# (2) We associate routes to this blueprint
@auth.route('/auth/register', methods=['GET'])
def get_register():
    """
    Route to register a new user.
    This new user can be a Runner, or a Trainer, but not an Admin.

    Details:
        There is no route to register an Admin, as it would be a major security flaw.
        Admins should be inserted by-hand in the database.
        There is also no route to register as a Runner, because a Runner has to be linked
        to a Trainer. Only the Trainer or the Admin can create an account for the Runner.
    """
    try:
        # if role not in ['trainer', 'runner']:
            # raise Exception("'role' should be either trainer, or runner.")

        users = db.session.query(User).all()
        json = []
        print(f"json value :: {users}")
        for r in users:
            json.append(r.json_out())
        return "<p>Hello, World goood!</p>"

    except sqlalchemy.exc.IntegrityError as err:
        logger.exception(f'Bad request: User already exists ({err}).')
        abort(Response(
            f'Bad request: User already exists.',
            HTTPStatus.BAD_REQUEST
        ))

    except Exception as err:
        logger.exception(f'Bad request: {err}')
        abort(Response(f'Bad request: {err}', HTTPStatus.BAD_REQUEST))