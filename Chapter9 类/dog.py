class Dog:
    """A simple attempt to simulate a puppy"""

    # Python will automatically run the method "__init__()" whenever a new instance is created from the class
    def __init__(self, name, age):
        """Initialize the attributes name and age"""
        self.name = name
        self.age = age
        # Variables prefixed with self are available to all methods in the class

    def sit(self):
        """Simulates a puppy crouching when commanded"""
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        """Simulates a puppy rolling when commanded"""
        print(self.name.title() + ' rolled over!')


# Create a new instance from the class defined above
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is ", my_dog.age,  " years old.")
# can be written in another form
# print("My dog is " + str(my_dog.age) + " years old.")
