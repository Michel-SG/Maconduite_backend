from maconduite_back.models.user import User
from http import HTTPStatus
import uuid


def test_create_user_in_database(app, db, client):
    with app.app_context():
        unique_id = uuid.uuid4().hex
        json_edited = {
            "email": f"mickael{unique_id}@yahoo.fr",
            "password": "michello",
            "first_name": "SADEU",
            "last_name": "NGAKOUo",
        }
        res = client.post(
            path="/auth/register",
            content_type="application/json",
            json=json_edited,
        )
        assert res.status_code == HTTPStatus.OK
        assert "access_token" in res.json
