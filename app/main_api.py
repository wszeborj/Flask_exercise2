from flask import Blueprint, request, jsonify
from . import db
from .models import Notes, NotesSchema

add_note_blueprint = Blueprint('add_note', __name__)
get_notes_blueprint = Blueprint('get_notes', __name__)
get_note_blueprint = Blueprint('get_note', __name__)
update_note_blueprint = Blueprint('update_note', __name__)
delete_note_blueprint = Blueprint('delete_note', __name__)

note_schema = NotesSchema()
notes_schema = NotesSchema(many=True)


def add_to_db(new_note: Notes) -> None:
    db.session.add(new_note)
    db.session.commit()


def delete_from_db(note_to_delete: Notes) -> None:
    db.session.delete(note_to_delete)
    db.session.commit()


@add_note_blueprint.route('/note', methods=['POST'])
def add_note() -> str:
    body = request.json

    new_note = Notes.create_from_json(json_body=body)

    add_to_db(new_note)

    return note_schema.jsonify(new_note)


@get_notes_blueprint.route('/notes', methods=['GET'])
def get_notes() -> str:
    all_notes = Notes.query.all()
    return notes_schema.jsonify(all_notes)


@get_note_blueprint.route('/note/<int:id>', methods=['GET'])
def get_note_by_id(id: int) -> str:
    found_note = Notes.query.get(id)
    return note_schema.jsonify(found_note)


@update_note_blueprint.route('/note/<int:id>', methods=['PUT'])
def update_note(id: int) -> str:
    found_note = Notes.query.get(id)

    body = request.json
    found_note.update(Notes.create_from_json(json_body=body))

    db.session.commit()

    return note_schema.jsonify(found_note)


@delete_note_blueprint.route('/note/<int:id>', methods=['DELETE'])
def delete_note(id: int) -> str:
    note_to_delete = Notes.query.get(id)
    delete_from_db(note_to_delete)

    return note_schema.jsonify(note_to_delete)
