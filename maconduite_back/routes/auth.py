from flask import Blueprint, request, jsonify, abort, Response, current_app
from http import HTTPStatus
import sqlalchemy
from maconduite_back.models.user import User
from maconduite_back.security import generate_token
from maconduite_back.security import auth_required
from maconduite_back.app import bcrypt
import logging

from maconduite_back.app import db

logger = logging.getLogger(__name__)
# (1) We instanciate the blueprint
auth = Blueprint("auth", __name__)


# (2) We associate routes to this blueprint
@auth.route("/auth/register", methods=["POST"])
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
        hashedpassword = bcrypt.generate_password_hash(json['password'], 10)
        new_user = User(
            email=json["email"],
            password=hashedpassword,
            first_name=json["first_name"],
            last_name=json["last_name"],
        )
        db.session.add(new_user)
        db.session.commit()

        new_token = generate_token(new_user.public_id, role="client")
        return {"access_token": new_token}, HTTPStatus.OK

    except sqlalchemy.exc.IntegrityError as err:
        logger.exception(f"Bad request: User already exists ({err}).")
        abort(Response(f"Bad request: User already exists.", HTTPStatus.BAD_REQUEST))

    except Exception as err:
        logger.exception(f"Bad request: {err}")
        abort(Response(f"Bad request: {err}", HTTPStatus.BAD_REQUEST))


@auth.route("/auth/login/<role>", methods=["POST"])
@auth_required(["admin", "client"])
def post_login(jwt, role):
    """
    Route to log in.
    """
    try:
        if role not in ["admin", "client"]:
            raise Exception("`role` should be one of [admin, client].")

        json = request.get_json()
        found_user = None

        if role == "admin":
            logger.info(f"Admin user")

            # found_user = Admin.query.filter(
            #     Admin.email == json['email'],
            #     Admin.public_id == jwt['public_id']
            # ).one_or_none()

        elif role == "client":
        
            user = User.query.filter(
                User.email == json["email"], User.public_id == jwt["public_id"]
            ).one_or_none()
            hashedpassword = bcrypt.generate_password_hash(json['password'], 10)
            logger.debug(f"User password end :: :: {user.password} :: ::user in :: :: {hashedpassword}")
            if user and bcrypt.check_password_hash(user.password,json['password']):
                found_user = user
            else:
                valluematch = {"data": "Wrong email or password."}
                return valluematch["data"], HTTPStatus.OK
        if found_user:
            logger.info(f"User #{found_user.public_id} authenticated successfully")
            logger.info(f'User email :: #{json["email"]}')
            return found_user.json_out(), HTTPStatus.OK

        else:
            raise ValueError("Wrong email or password.")

    except Exception as err:
        logger.exception(f"Bad request: {err}")
        abort(Response(f"Bad request: {err}", HTTPStatus.BAD_REQUEST))
