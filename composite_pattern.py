class Component(object):
    """Abstract class"""

    def __init__(self, *args, **kwargs) -> None:
        pass

    def component_function(self):
        pass

class Child(Component): # Inherits from the abstract class, Component
    """Concrete class"""

    def __init__(self, *args, **kwargs) -> None:
        Component.__init__(self, *args, **kwargs)
        self.name = args[0]

        # This function is where we store the same of your child item!
    
    def component_function(self):
        # Print hte name of your child item here
        print(f"{self.name}")

class Composite(Component):# Inherits from the abstract class, Component
    """Concrete class and maintains the tree recursive structure"""

    def __init__(self, *args, **kwargs) -> None:
        Component.__init__(*args, **kwargs)

        # This is where we store the name of the composite object
        self.name = args[0]

        #This is where we keep the child items
        self.children = []

    def apppend_child(self, child):
        """Method to add a new child item"""
        self.children.append(child)
    
    def remove_child(self, child):
        """Method to remove child item"""
        self.children.append(child)
    
    def component_function(self):
        # Print hte name of your child item here
        print(f"{self.name}")

        for i in self.children:
            i.component_function()


if __name__ == "__main__":

    sub1 = Composite("submenu1")

    sub11 = Child("sub_submenu 11")
    sub12 = Child("sub_submenu 12")

    sub1.apppend_child(sub11)
    sub1.apppend_child(sub12)

    top = Composite("top_menu")

    sub2 = Child("submenu2")

    top.apppend_child(sub1) # Composite child items
    top.apppend_child(sub2) # Plain child items


    top.component_function()