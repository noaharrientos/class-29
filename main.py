from abc import ABC , abstractmethod
class studentclass(ABC):
    def display(self,name):
        print(f"The name is {name}")
    @abstractmethod
    def name1(self):
        print(f"This is the method of abstract method")
class inheritance(studentclass):
    def name1(self):
        print(f"This is a method of the child class")
object1 = inheritance()
object1.display("Jacob")
object1.name1()