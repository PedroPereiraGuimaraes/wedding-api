import os
from dotenv import load_dotenv
import pymongo

load_dotenv()

class Database:
    def __init__(self, collection):
        database = os.getenv('DB_NAME')
        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            user = os.getenv('DB_USER')
            password = os.getenv('DB_PASSWORD')

            uri = f"mongodb+srv://{user}:{password}@api.qz86w.mongodb.net/?retryWrites=true&w=majority&appName=API"
            
            self.cluster_connection = pymongo.MongoClient(
                uri,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.cluster_connection[database]
            self.collection = self.db[collection]
            print('Connected to the database successfully!')
        except Exception as e:
            print('Error while trying to connect to the database:', e)
