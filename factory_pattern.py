class Dog:

    """ a simple dog class"""

    def __init__(self, name) -> None:
        self._name = name

    def speak(self):
        return "Woof!"
    
class Cat:

    """ a simple cat class"""

    def __init__(self, name) -> None:
        self._name = name

    def speak(self):
        return "Meow!"
    

def get_pet(pet="dog"): # Factory Method

    """The factory method.
        Creates objects and return them to the user
    """
    
    pets = dict(
        dog=Dog("Hope"),
        cat=Cat("Peace")
        )
    return pets[pet]

if __name__ == "__main__":
    d = get_pet("dog")
    print(d.speak())

    c = get_pet("cat")
    print(c.speak())