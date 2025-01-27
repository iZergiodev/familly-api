from flask_sqlalchemy import SQLAlchemy
from extension import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    done = db.Column(db.Boolean(), nullable=False)
    label = db.Column(db.String(50), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'done': self.done,
            'label':self.label,
        }
    



