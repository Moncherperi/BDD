from api.note_client import NoteClient

def before_all(context):
    context.client = NoteClient("http://127.0.0.1:8000")

def before_scenario(context, scenario):
    response = context.client.get_notes()
    if response.status_code == 200:
        notes = response.json()
        for note in notes:
            context.client.delete_note_by_id(note['id'])
