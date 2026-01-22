
from app import app
from models import db, Pet
from sqlalchemy import func

def demo():
    with app.app_context():
        # 1. Create a new instance of the model class Pet
        print("--- Adding Fido ---")
        pet1 = Pet(name="Fido", species="Dog")
        print(f"Before add: {pet1}")
        
        # 2. Add the Pet instance to the current database session
        db.session.add(pet1)
        print(f"After add (before commit) id: {pet1.id}")
        
        # 3. Commit the transaction
        db.session.commit()
        print(f"After commit id: {pet1.id}")
        
        # Add another pet
        print("\n--- Adding Whiskers ---")
        pet2 = Pet(name="Whiskers", species="Cat")
        db.session.add(pet2)
        db.session.commit()
        print(f"Added: {pet2}")
        
        # Querying
        print("\n--- Querying all pets ---")
        all_pets = Pet.query.all()
        print(all_pets)
        
        print("\n--- Querying first pet ---")
        first_pet = Pet.query.first()
        print(first_pet)
        
        # Filtering
        print("\n--- Filtering by species='Cat' ---")
        cats = Pet.query.filter(Pet.species == 'Cat').all()
        print(cats)
        
        print("\n--- Filtering name starts with 'F' ---")
        f_pets = Pet.query.filter(Pet.name.startswith('F')).all()
        print(f_pets)
        
        # filter_by
        print("\n--- filter_by species='Cat' ---")
        cats_by = Pet.query.filter_by(species='Cat').all()
        print(cats_by)
        
        # get
        print("\n--- get Pet by id=1 ---")
        p1 = db.session.get(Pet, 1)
        print(p1)
        
        # order_by
        print("\n--- ordering by species ---")
        ordered = Pet.query.order_by('species').all()
        print(ordered)
        
        # func.count
        print("\n--- counting pets ---")
        count = db.session.query(func.count(Pet.id)).first()
        print(f"Total pets: {count[0]}")
        
        # update
        print("\n--- updating Fido ---")
        pet1.name = "Fido the mighty"
        db.session.commit()
        print(f"Updated: {Pet.query.get(pet1.id)}")
        
        # delete
        print("\n--- deleting Fido ---")
        db.session.delete(pet1)
        db.session.commit()
        print(f"Remaining pets: {Pet.query.all()}")
        
        # delete all
        print("\n--- deleting all pets ---")
        Pet.query.delete()
        db.session.commit()
        print(f"Final pets count: {Pet.query.count()}")

if __name__ == "__main__":
    demo()
