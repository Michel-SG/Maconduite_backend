from maconduite_back.models.user import User
from http import HTTPStatus
import uuid


def test_login_user_in_database(app, db, client):
    with app.app_context():
        unique_id = uuid.uuid4().hex
        json_edited = {
            "email": f"franck{unique_id}@yahoo.fr",
            "password": "franck",
            "first_name": "franck",
            "last_name": "franck NGAKOUo",
        }
        res = client.post(
            path="/auth/register",
            content_type="application/json",
            json=json_edited,
        )
        assert res.status_code == HTTPStatus.OK
        assert "access_token" in res.json

        res_login = client.post(
            path="/auth/login/client",
            headers={"Authorization": "Bearer " + res.json["access_token"]},
            content_type="application/json",
            json=json_edited,
        )
        assert res_login.status_code == HTTPStatus.OK
