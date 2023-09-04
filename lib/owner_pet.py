class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    def __init__(self, name, pet_type, owner = None):
        self.name = name
        self.owner = owner

        if pet_type in Pet.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception
        
        Pet.all.append(self)

class Owner:
    
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return str(self)

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception
        pet.owner = self

    def get_sorted_pets(self):
        pets = [pet for pet in Pet.all]
        def sort_key(e):
            return e.name
        return sorted(pets, key=sort_key)

