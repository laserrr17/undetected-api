import requests
import json
import tkinter as tk
from tkinter import scrolledtext

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
        'api-key': 'Your API Key',
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
        'api-key': 'Your API Key',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json().get('output')
    else:
        print("Error retrieving document:", response.text)
        return None

class UndetectedApp:
    def __init__(self, master):
        self.master = master
        master.title("Undetected API Interface")

        # Text input area
        self.text_area = scrolledtext.ScrolledText(master, wrap = tk.WORD, width = 40, height = 10)
        self.text_area.pack(pady=10)

        # Submit Button
        self.submit_button = tk.Button(master, text="Submit Text", command=self.submit_text)
        self.submit_button.pack(pady=5)

        # Retrieve Button
        self.retrieve_button = tk.Button(master, text="Retrieve Text", command=self.retrieve_text)
        self.retrieve_button.pack(pady=5)

        # Display area
        self.display_area = scrolledtext.ScrolledText(master, wrap = tk.WORD, width = 40, height = 10, state='disabled')
        self.display_area.pack(pady=10)

    def submit_text(self):
        # Get text from text_area
        input_text = self.text_area.get("1.0", tk.END)
        document_id = submit_document(input_text)
        self.display_area.config(state='normal')
        self.display_area.delete('1.0', tk.END)
        self.display_area.insert(tk.END, "Submitted. Document ID: " + str(document_id))
        self.display_area.config(state='disabled')

    def retrieve_text(self):
        # Get the last document ID (for simplicity)
        # In a full application, you'd want to manage document IDs more robustly
        document_id = self.display_area.get("1.0", tk.END).split()[-1]
        retrieved_text = retrieve_document(document_id)
        self.display_area.config(state='normal')
        self.display_area.delete('1.0', tk.END)
        self.display_area.insert(tk.END, "Retrieved Text: \n" + retrieved_text)
        self.display_area.config(state='disabled')

# Create the main window and pass it to the Application
root = tk.Tk()
app = UndetectedApp(root)
root.mainloop()
