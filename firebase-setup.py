import firebase_admin
from firebase_admin import credentials, firestore
import os


# Path to your service account key file
cred_path = os.getenv('FIREBASE_ADMIN_CREDENTIALS_PATH')
if not cred_path:
    raise ValueError("The environment variable FIREBASE_ADMIN_CREDENTIALS_PATH is not set.")
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# Test writing to Firestore
def test_write():
    doc_ref = db.collection('testCollection').document('testDocument')
    doc_ref.set({
        'name': 'Test User',
        'email': 'testuser@example.com'
    })
    print("Document written successfully.")

# Test reading from Firestore
def test_read():
    doc_ref = db.collection('testCollection').document('testDocument')
    doc = doc_ref.get()
    if doc.exists:
        print(f"Document data: {doc.to_dict()}")
    else:
        print("No such document!")

if __name__ == "__main__":
    test_write()
    test_read()