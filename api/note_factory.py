from models import Note


class NoteFactory:

    @staticmethod
    def create_valid_payload():
        return {"title": "Valid Title", "content": "Valid Content"}

    @staticmethod
    def create_invalid_payload():
        return {"title": "", "content": "Invalid Content"}






