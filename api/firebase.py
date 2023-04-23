import json

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from config_provider import config


class Firebase:

    def __init__(self):
        # Init firebase connection.
        cred = credentials.Certificate(config.get_firebase_credentials_file())
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def add_document(self, collection, data):
        self.db.collection(collection).add(data)

    def update_document(self, collection, document, data):
        doc_ref = self.db.collection(collection).document(document)
        doc_ref.update(data)

    def get_document(self, collection, document):
        result = {}
        doc_ref = self.db.collection(collection).document(document)

        try:
            doc = doc_ref.get()
            if doc.exists:
                result = doc.to_dict()
            else:
                print('Document', document, "in collection", collection, "does not exist.")
        except Exception as e:
            print("Error getting document:", e)
        return result


firebase = Firebase()
