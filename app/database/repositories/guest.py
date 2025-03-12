from app.database.connection import Database
from app.models.guest import Guest

class GuestDAO:
    def __init__(self):
        self.db = Database(collection='guests')

    def create(self, guest: Guest):
        try:
            search = self.db.collection.find_one({"email": guest.email})
            
            if search:
                return {"error": "Guest already exists."}, 400

            guest_dict = guest.model_dump(exclude_unset=True)
            result = self.db.collection.insert_one(guest_dict)

            if result.acknowledged:
                return {"message": "Guest created successfully."}, 201
            else:
                return {"error": "Failed to create guest."}, 500
        except Exception as e:
            return {"error": f"There was an error when trying to create a new guest: {str(e)}"}, 500
        
    def get(self, token: str):
        try:
            guest_data = self.db.collection.find_one({"token": token})
            
            if guest_data:
                return Guest(**guest_data).to_dict(), 200
            else:
                return {"error": "Token does not exist."}, 404
        except Exception as e:
            return {"error": f"There was an error when trying to fetch the guest by token: {str(e)}"}, 500

    def update(self, guest: Guest):
        try:
            search = self.db.collection.find_one({"token": guest.token})

            if not search:
                return {"error": "Token does not exist."}, 404

            guest_dict = guest.model_dump(exclude_unset=True)
            self.db.collection.update_one({"token": guest.token}, {"$set": guest_dict})

            return {"message": "Guest updated successfully."}, 200
        except Exception as e:
            return {"error": f"There was an error when trying to update the guest: {str(e)}"}, 500
        
    def get_confirmed(self):
        try:
            status = []

            for guest in self.db.collection.find():
                status.append({
                    "name": guest.get("accountable"),
                    "age": guest.get("age"),
                    "confirmed": guest.get("confirmed")
                })

                for dependent in guest.get("dependents", []):
                    status.append({
                        "name": dependent.get("name"),
                        "age": dependent.get("age"),
                        "confirmed": dependent.get("confirmed")
                    })

            if status:
                return status, 200
            else:
                return {"message": "No confirmed guests or dependents found."}, 404
        except Exception as e:
            return {"error": f"There was an error when trying to fetch confirmed guests and dependents: {str(e)}"}, 500