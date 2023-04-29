from lexicon_legends import db, login_manager
from flask_login import UserMixin
                                                
                                                
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
                                                
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    rank = db.Column(db.Integer, nullable=False, default=0)
                                                
    def __repr__(self):
        return f"User('{self.key}', '{self.username}', '{self.email}')"
                                                
                                                