class Dog:

    """ One of object to be returned"""

    def speak(self):
        return "Woof!"
    
    def __str__(self) -> str:
        return "Dog"
    
class Cat:

    """ One of object to be returned"""

    def speak(self):
        return "Meow!"
    
    def __str__(self) -> str:
        return "Cat"

class CatFactory:
    """Concrete Factory"""

    def get_pet(self):
        """Returns a Cat object"""
        return Cat()

    def get_food(self):
        """Returns a cat food object"""
        return "Cat food!"
    
class DogFactory:

    """Concrete Factory
       Creates to related items (instead of one Object like factory_pattern example)
    """

    def get_pet(self):
        """Returns a Dog object"""
        return Dog()
        

    def get_food(self):
        """Returns a dog food object"""
        return "Dog food!"
    
class PetStore:
    """ PetStore houses our Abstract Factory """

    def __init__(self, pet_factory=None) -> None:
        """ pet_factory is our Abstract Factory """
        self._pet_factory = pet_factory
    def show_pet(self):
        """ Utility method to display the details of the object returned"""

        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print(f"Our pet is '{pet}!")
        print(f"Our pet says hello by '{pet.speak}!")
        print(f"It's foode is  '{pet_food}!")

if __name__ == '__main__':
    # Create a concrete factory
    factory = DogFactory()
    factory2 = CatFactory()
    #Create a pet store housing our Abstract Factory
    shop = PetStore(factory)
    shop2 = PetStore(factory2)

    # Invoce utility method to show details of our pet 
    shop.show_pet()
    print("-"*10)
    shop2.show_pet()