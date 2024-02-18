import uuid
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from maconduite_back.app import db

class User(db.Model):
    """
    Admin is a user which can access all ressources.
    """
    __tablename__ = 'user'

    # PRIVATE PROPERTIES: they are not shared outside of the backend
    id            = db.Column(db.Integer,   primary_key=True)
    created_at    = db.Column(db.DateTime,  nullable=False)
    email         = db.Column(db.Text,      nullable=False, unique=True)
    password      = db.Column(db.Text,      nullable=False)

    # public properties: they are sent to the front-end in JSON-format
    public_id     = db.Column(db.Text,      nullable=False, unique=True)
    first_name    = db.Column(db.Text,      nullable=True)
    last_name     = db.Column(db.Text,      nullable=True)


    def __init__(self, email, password, first_name=None, last_name=None):
        super(type(self))
        self.public_id = uuid.uuid4().hex
        self.created_at = datetime.now()
        self.email = email
        self.password = password
        self.first_name  = first_name
        self.last_name   = last_name


    def __repr__(self):
        return f"<User {self.id} - {self.email}:{self.password} #{self.public_id}>"


    def json_out(self):
        """
        These are the parameters that will be sent in a response, after a GET/POST/PUT.
        Only the public properties are sent, the private properties should NOT be shared
        outside of the backend.
        """
        json = {
            "public_id"   : self.public_id,
            "first_name"  : self.first_name,
            "last_name"   : self.last_name,
        }
        return json
