# Define a class called NetDevice
class NetDevice:
    # Define the constructor method __init__ which initializes object attributes
    def __init__(self = '?', name = '?' ,location = '?', type = '?', swVersion = '?'):
        # Initialize object attributes with default values or values provided during object creation
        self.Name = name
        self.Location = location
        self.Type = type
        self.SwVersion = swVersion
    
    # Define a method called PrintAttributes to print object attributes
    def PrintAttributes(self):
        # Print a formatted string displaying the device name and its attributes
        print(F'The device {self.Name} has the following attributes\n')
        # Print the dictionary containing all attributes of the object
        print(F'\t --> :{self.__dict__} \n')

# Create an instance of the NetDevice class with specific attribute values
NewNetDevice = NetDevice(name='RouterXXX', swVersion='Ac23848')

# Call the PrintAttributes method to print the attributes of the NewNetDevice object
NewNetDevice.PrintAttributes()

