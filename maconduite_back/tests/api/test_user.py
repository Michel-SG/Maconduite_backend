from maconduite_back.models.user import User
from http import HTTPStatus
import uuid


def test_create_user(app, db, client):
    with app.app_context():
        unique_id = uuid.uuid4().hex
        new_user = User(
            email=f"uguello{unique_id}@gmail.com",
            password="uguel",
            first_name="SADEU Ugue",
            last_name="NGAKOU michel",
        )
        db.session.add(new_user)
        db.session.commit()
        user = User.query.filter_by(password="uguel").first()
        assert user.last_name == new_user.last_name
        
