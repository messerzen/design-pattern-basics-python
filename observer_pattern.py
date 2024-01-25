class Subject(object): # Represents what is beign 'observerd'
    def __init__(self) -> None:
        self._observers = [] # This is where references to all the observers
                             # Note that this is a one-to-may relationship
        
    def attach(self, observer):
        # If the observer is nt already in the observer list
        # append the observer to the list
        if observer not in self._observers:
            self._observers.append(observer)
        

    def detach(self, observer): #Remove the observer
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:# For all the obeserver in the list
            if modifier != observer: # Don't modify the observers who is actually updating the temperature
                observer.update(self)  # Alert the observers

class Core(Subject):

    def __init__(self, name="") -> None:
        super().__init__()
        self._name = name # Set the name of the core 
        self._temp = 0

        @property
        def temp(self):
            return self._temp
        
        @temp.setter
        def temp(self, temp):
            self._temp = temp
            # Notify the obsever whenever someone changes the temperature
            self.notify()
            

class TempViwer:

    def update(self, subject): # Alert method that is invocek when the temperature value changes
        print(f"Temperature viwer: {subject} has temperature {subject.temp}")
            
if __name__ == "__main__":
    # Subjects
    c1 = Core("Core 1")
    c2 = Core("Core 2")
    # Observers
    v1 = TempViwer()
    v2 = TempViwer()

    # Attach the observes to 1st core
    c1.attach(v1)
    c1.attach(v2)

    c1.temp = 80
    c1.temp = 90

    print(c1._temp)