import time

class Producer:
    """Define the 'resource-intensive' object to instantiate!"""
    def produce(self):
        print("Producer is working hard")

    def meet(self):
        print("Producer has time to met you now")

class Proxy:
    """Define the 'relatively less resource-intensive' proxy to instantiate"""
    def __init__(self) -> None:
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        """Check if producer is available"""
        print("Artist checking if producer is available ...")

        if self.occupied == 'No':
            # If the producer is available, create a producer object
            self.producer = Producer()
            time.sleep(3)
            # Make the producer meet the guest!
            self.producer.meet()

        else:
            # Otherwise, don't instantiate a producer
            time.sleep(2)
            print("Producer is busy!")

if __name__ == "__main__":
    #Instantiate a proxy
    p = Proxy()

    #Make the proxy Artist produce until Producer is available
    p.produce()

    # Change state to occupied
    p.occupied = 'Yes'
    # Make the producer produce 
    p.produce()