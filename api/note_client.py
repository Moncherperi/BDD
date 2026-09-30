import requests

class NoteClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def create_note(self, payload):
        url = self.base_url + '/notes'
        return requests.post(url, json=payload)

    def get_notes(self):
        url = self.base_url + '/notes'
        return requests.get(url)

    def get_note_by_id(self, note_id):
        url = self.base_url + '/notes/' + str(note_id)
        return requests.get(url)

    def update_note_by_id(self, payload, note_id):
        url = self.base_url + '/notes/' + str(note_id)
        return requests.put(url, json=payload)

    def delete_note_by_id(self, note_id):
        url = self.base_url + '/notes/' + str(note_id)
        return requests.delete(url)


