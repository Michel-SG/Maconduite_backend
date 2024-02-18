from maconduite_back.models.user import User

def test_create_user(app,db):
    with app.app_context():
        new_user = User(email='mickael', password="michello", first_name='SADEU', last_name='NGAKOUo')
        db.session.add(new_user)
        db.session.commit()
        user = User.query.filter_by(password = "michello").first()
        users = User.query.all()
        assert user.email == 'mickael'
        assert len(users) == 1

def test_get_method(client):
    response = client.get('/auth/register')
    assert b'<p>Hello, World goood!</p>' in response.data