from database.connection import Database
from app.models.gift import Gift

class GiftDAO:
    def __init__(self):
        self.db = Database(collection='gifts')

    def create(self, gift: Gift):
        try:
            search = self.db.collection.find_one({"name": gift.name})
            
            if search:
                return {"error": "Gift already exists."}, 400

            gift_dict = gift.model_dump(exclude_unset=True)
            result = self.db.collection.insert_one(gift_dict)
            
            if result.acknowledged:
                return {"message": "Gift created successfully."}, 201
            else:
                return {"error": "Failed to create gift."}, 500
        
        except Exception as e:
            return {"error": f"There was an error when trying to create a new gift: {str(e)}"}, 500
        
    def get(self):
        try:
            gift_data = self.db.collection.find()
            
            if gift_data:
                gifts = [Gift(**gift).to_dict() for gift in gift_data]
                return gifts, 200
            else:
                return {"error": "No gifts found."}, 404
        
        except Exception as e:
            return {"error": f"There was an error when trying to fetch the gifts: {str(e)}"}, 500