import requests
import json
import time

# Function to submit the document and get the document ID
def submit_document(content):
    url = "https://api.undetectable.ai/submit"
    payload = json.dumps({
        "content": content,
        "readability": "High School",
        "purpose": "General Writing",
        "strength": "More Human"
    })
    headers = {
        'api-key': '1698466102307x152869854390923940',
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json().get('id')
    else:
        print("Error submitting document:", response.text)
        return None

# Function to retrieve the document
def retrieve_document(document_id):
    url = "https://api.undetectable.ai/document"
    payload = json.dumps({
        "id": document_id
    })
    headers = {
        'api-key': '1698466102307x152869854390923940',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json().get('output')
    else:
        print("Error retrieving document:", response.text)
        return None

# Main script
user_content = input("Please enter the content: ")
document_id = submit_document(user_content)

if document_id:
    print("Document submitted. ID:", document_id)
    print("Waiting for document to be processed...")
    time.sleep(30)  # Wait for the document to be processed

    document = retrieve_document(document_id)
    if document:
        print("Retrieved Document:", document)
