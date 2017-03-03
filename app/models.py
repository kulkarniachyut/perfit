from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import jwt
from app import db, login_manager

class Users(UserMixin, db.Model):
    """
    Create an Employee table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    # username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True,nullable=False)
    last_name = db.Column(db.String(60), index=True)
    email_id = db.Column(db.String(60), index=True, unique=True,nullable=False)
    dob = db.Column(db.Date)
    phone = db.Column(db.Integer, unique=True)
    gender = db.Column(db.Binary(1))
    oauth_id = db.Column(db.String(256), unique = True)
    password_hash = db.Column(db.String(128),nullable=False)
    confirmation_status = db.Column(db.Boolean(1))
    x_auth_token = db.Column(db.String(256),unique=True,nullable=False)
    created_at = db.Column(db.TIMESTAMP,nullable=False);
    # department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    # role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    # is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.email_id)

    def encode_auth_token(self, user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=100, seconds=0),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                app.config.get('KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
