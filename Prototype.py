import copy

class Prototype:

    def __init__(self) -> None:
        self._objects = {}

    def register_object(self, name, obj):
        """Register an object"""

        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""

        del self._objects[name]

    def clone(self, name, **attr):
        """Clone a registered object and updates its attributes"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj

class Car:

    """ Product """
    def __init__(self) -> None:
        self.model = "Skylark"
        self.color = "Red"
        self.options = "Ex"

    def __str__(self) -> str:
        return f" {self.model} | {self.color} | {self.options} "
    

if __name__ == "__main__":

    c = Car() # Prototipcal object to be cloned 
    prototype = Prototype()
    prototype.register_object('skylark', c)
    c1 = prototype.clone('skylark', color="Blue")
    print(c1)
    # c1 = prototype.clone('skylark', engine="v6")
    # print(c1.__getattribute__('engine'))


    

