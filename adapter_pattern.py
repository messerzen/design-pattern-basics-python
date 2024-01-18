from typing import Any


class Korean:
    """Korean speaker"""
    def __init__(self) -> None:
        self.name = "Korean"

    def speak_korean(self):
        return "An-neyong?"

class British:
    """English speaker"""
    def __init__(self) -> None:
        self.name = "British"
    
    def speak_english(self):
        return "Hello"
    
class Adapter:
    """This changes the generic method name to individualized method name"""

    def __init__(self, object, **adapted_method) -> None:
        """change the name of method"""
        self._object = object

        # Add a new dictionary item that establishes the mapping between generic method name an concrete method name
        # speak() will be translate to speak_korean

        self.__dict__.update(adapted_method)

    def __getattr__(self, attr) -> Any:
        """Simply return the rest of attributes"""
        return getattr(self._object, attr)
                       
# List to store speaker objects
objects = []


# Create a korean object
korean = Korean()
# Create a british object
british = British()

# Append the object to the object list
objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))

for obj in objects:

    print(f"{obj.name} says {obj.speak()}")