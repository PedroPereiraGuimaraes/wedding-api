from database.connection import Database
from models.guest import Guest

class GuestDAO:
    def __init__(self):
        self.db = Database(collection='guests')

    def create(self, guest: Guest):
        try:
            search = self.db.collection.find_one({"email": guest.email})
            
            if search:
                print("Guest already exists.")
                return False

            guest_dict = guest.model_dump(exclude_unset=True)
            result = self.db.collection.insert_one(guest_dict)

            return result.acknowledged
        except Exception as e:
            print(f'There was an error when trying to create a new guest: {e}')
            return None
        
    def get(self, token: str):
        try:
            guest_data = self.db.collection.find_one({"token": token})
            
            if guest_data:
                return Guest(**guest_data) 
            else:
                print("Token not exists.")
                return None
        except Exception as e:
            print(f'There was an error when trying to fetch the guest by token: {e}')
            return None

    def update(self, guest: Guest):
        try:
            search = self.db.collection.find_one({"token": guest.token})

            if not search:
                print("Token not exists.")
                return None

            guest_dict = guest.model_dump(exclude_unset=True)

            self.db.collection.update_one({"token": guest.token}, {"$set": guest_dict})

            return {"message": "Guest updated successfully."}
        except Exception as e:
            print(f'There was an error when trying to update the guest: {e}')
            return None
        
    def get_confirmed(self):
        try:
            all_guests_status = []

            for guest in self.db.collection.find():
                all_guests_status.append({
                    "name": guest.get("accountable"),
                    "age": guest.get("age"),
                    "confirmed": guest.get("confirmed")
                })

                for dependent in guest.get("dependents", []):
                    all_guests_status.append({
                        "name": dependent.get("name"),
                        "age": dependent.get("age"),
                        "confirmed": dependent.get("confirmed")
                    })

            return all_guests_status

        except Exception as e:
            print(f'There was an error when trying to fetch confirmed guests and dependents: {e}')
            return None
