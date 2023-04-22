import requests

from config_provider import config
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from config_provider import config

class Firebase:

    def __init__(self):
        # Use a service account.
        cred = credentials.Certificate(config.get_firebase_credentials_file())
        firebase_admin.initialize_app(cred)

        # Get document from database.
        self.db = firestore.client()
        pass

    def get_overrides(self):
        pass

    def test(self):
        # Get document from database.
        doc_ref = self.db.collection(u'override').document(u'override_light')

        try:
            doc = doc_ref.get()
            if doc.exists:
                print(f'Document data: {doc.to_dict()}')
            else:
                print(u'No such document!')
        except Exception as e:
            print("Error getting document:", e)


firebase = Firebase()

# Test - Remove later
firebase.test()
