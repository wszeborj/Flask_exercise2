from __future__ import annotations
from . import db, ma
from flask_marshmallow import fields
from datetime import datetime


class Notes(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(length=50), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    data = db.Column(db.String(length=5000), nullable=True)

    def __init__(self, author: str, date: datetime, data: str):
        self.author = author
        self.date = date
        self.data = data

    def update(self, modified_note: Notes) -> None:
        self.author = modified_note.author
        self.date = modified_note.date
        self.data = modified_note.data

    @staticmethod
    def create_from_json(json_body: dict) -> Notes:
        if 'date' not in json_body:
            date = datetime.utcnow()
        else:
            date = datetime.strptime(json_body['date'], '%d/%m/%y')

        return Notes(author=json_body['author'],
                     date=date,
                     data=json_body['data']
                    )


class NotesSchema(ma.Schema):
    _id = fields.fields.Integer()
    author = fields.fields.Str()
    date = fields.fields.DateTime(format='%d-%m-%y')
    data = fields.fields.Str()
