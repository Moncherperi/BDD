Feature: Create a note

Scenario: Successfully create a note
Given the note payload with title "Test" and content "This is a note"
When I send a request to create the note
Then the response status code should be 200
And the response should contain the correct title


Scenario: Unsuccessfully create a note
Given the note payload with title "empty" and content "This is a note"
When I send a request to create the note
Then the response status code should be 200
And the response should contain the correct title


Scenario: Get all notes when the list is empty
Given the data is empty
When I send a request to get all notes
Then the response status code should be 200
And the response should return an empty list


Scenario: Get all notes when the list is not empty
Given the data contains notes
When I send a request to get all notes
Then the response status code should be 200
And the response should contain a list of notes


Scenario: Get the note by existed id
Given a note with id 1 exists
When I send a request to get the note with id 1
Then the response status code should be 404
And the response should have id 1


Scenario: Get the note by non-existed id
Given a note with id 999 does not exist
When I send a request to get the note with id 999
Then the response status code should be 404
And the response should contain error message


Scenario: Update the note by existed id
Given a note with id 1 exists
And the new note payload with title "Updated Title" and content "Updated Content"
When I send a request to update the note with id 1
Then the response status code should be 404
And the response should contain the updated title


Scenario: Update the note by non-existed id
Given a note with id 999 does not exist
And the new note payload with title "Updated Title" and content "Updated Content"
When I send a request to update the note with id 999
Then the response status code should be 404
And the response should contain error message


Scenario: Successfully delete the note by existed id
Given a note with id 1 exists
When I send a request to delete the note with id 1
Then the response status code should be 404
And the response should confirm deletion


Scenario: Delete the note by non-existed id
Given a note with id 999 does not exist
When I send a request to delete the note with id 999
Then the response status code should be 404
And the response should contain error message