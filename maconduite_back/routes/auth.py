from flask import Blueprint, request, jsonify, abort, Response, current_app
from http import HTTPStatus
import sqlalchemy
from maconduite_back.models.user import User
from maconduite_back.security import generate_token
import logging
from maconduite_back.app import db

logger = logging.getLogger(__name__)
# (1) We instanciate the blueprint
auth = Blueprint('auth', __name__)

# (2) We associate routes to this blueprint
@auth.route('/auth/register', methods=['POST'])
def post_register():
    """
    Route to register a new user.
    This new user can be a client, but not an Admin.

    Details:
        There is no route to register an Admin, as it would be a major security flaw.
        Admins should be inserted by-hand in the database.
    """
    try:  
        
        json = request.get_json()
        # if role == 'client':
        new_user = User(email=json['email'], password='michel', first_name=json['first_name'], last_name=json['last_name'])
        db.session.add(new_user)
        db.session.commit()

        # new_token = generate_token(new_user.public_id, role="client")
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