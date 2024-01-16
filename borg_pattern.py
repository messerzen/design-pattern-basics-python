class Borg:

    """ The borg design pattern 
        Object Oriented form of Global Variables
    """

    _shared_data = {} # Attribute dictionary

    def __init__(self) -> None:
        self.__dict__ = self._shared_data # Make an attribute dictionary

class Singleton(Borg):

    """ 
    The singleton class.
    The Borg attributes is shared among all classes that inherit Borg Class
    """

    def __init__(self, **kwargs) -> None:
        Borg.__init__(self)
        self._shared_data.update(kwargs) # Update the attribute dictionary by insertnig a new key-value pair


    def __str__(self) -> str:
        return str(self._shared_data) # Returns the attribute dictionary for printing
    

if __name__ == "__main__":
    # Creating a singleto Object and add our first acronym
    
    x = Singleton(HTTP = "Hyper Text Transfer Protocol")
    print(x)

    y = Singleton(TYPE = "application/JSON")

    print(y)