import firebase_admin
from firebase_admin import credentials, firestore

# Path to your service account key file
cred = credentials.Certificate('my-awesome-portfolio-pro-55988-firebase-adminsdk-vgp73-d698ccf7fd.json')
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