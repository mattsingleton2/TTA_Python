from abc import ABC, abstractclassmethod


#   Let's set up an abstract parent class.
class Computer(ABC):
    #   Here, we're telling the interpreter to relax...
    #   This method will be defined later in classes that inherit.
    @abstractclassmethod
    def process():
        #   Telling the interpreter 'pass' means we're good to go and keep rolling.
        pass
    
#   Important: That said, we can't instantiate an object of the abstract parent class
#               without the method being defined. This makes me scratch my head about
#               maintaining polymorphism.

#   Anyway, let's write a class to inherit from Computer.
class Laptop(Computer):
    #   Now we need to define the process() method.
    def process(self):
        print('The laptop quickly processes the data...')
    
    
#   Wrapping things up so we can instantiate and test...


if __name__ == "__main__":
#    obj1 = Computer() won't work since the abstract method isn't defined.
    obj2 = Laptop()
    #   This will work since the abstract method has definition...
    obj2.process()
    
    