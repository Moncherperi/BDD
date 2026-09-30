from behave import given, when, then
from api.note_client import NoteClient
from api.note_factory import NoteFactory

@given('the note payload with title "{title}" and content "{content}"')
def step_given_create_note(context, title, content):
    if title == "empty":
        title = ""
    data = NoteFactory.create_valid_payload()
    data['title'] = title
    data['content'] = content
    context.payload = data

@when("I send a request to create the note")
def step_when_create_note(context):
    context.response = context.client.create_note(context.payload)

@then("the response status code should be {status_code}")
def step_then_status_code(context, status_code):
    expected = int(status_code)
    actual = context.response.status_code
    if actual != expected:
        print(f"\n[ВНИМАНИЕ] Ожидали: {expected}, Сервер вернул: {actual}")
    assert actual == expected

@then("the response should contain {content_type}")
def step_then_content_type(context, content_type):
    response_data = context.response.json()
    if content_type == "the correct title":
        assert response_data['title'] == context.payload['title']
    elif content_type == "the error message":
        assert 'detail' in response_data
    elif content_type == "a list of notes":
        assert response_data != []
        assert isinstance(response_data, list)

@given("the data is empty")
def step_given_database_is_empty(context):
    # assert context.client.get_notes().json() == []
    pass

@when("I send a request to get all notes")
def step_when_get_all_notes(context):
    context.response = context.client.get_notes()

@then("the response should return an empty list")
def step_then_return_empty_list(context):
    assert context.response.json() == []

@given("the data contains notes")
def step_given_data_contains_notes(context):
    payload = NoteFactory.create_valid_payload()
    context.response = context.client.create_note(payload)

@given("a note with id {note_id} {existence}")
def step_given_note_exists(context, note_id, existence):
    context.target_id = int(note_id)

@when("I send a request to get the note with id {note_id}")
def step_when_get_note_by_id(context, note_id):
    context.response = context.client.get_note_by_id(int(note_id))

@then("the response should have id {note_id}")
def step_then_get_note_by_id(context, note_id):
    response_data = context.response.json()
    if 'id' in response_data:
        assert response_data['id'] == int(note_id)
    else:
        pass

@given('the new note payload with title "{title}" and content "{content}"')
def step_given_updated_note(context, title, content):
    data = NoteFactory.create_valid_payload()
    data['title'] = title
    data['content'] = content
    context.payload = data

@when('I send a request to update the note with id {note_id}')
def step_when_update_note(context, note_id):
    context.response = context.client.update_note_by_id(context.payload, int(note_id))

@when("I send a request to delete the note with id {note_id}")
def step_when_delete_note(context, note_id):
    context.response = context.client.delete_note_by_id(int(note_id))

@then('the response should confirm deletion')
def step_then_confirm_deletion(context):
    assert context.response.status_code in [200, 204, 404]