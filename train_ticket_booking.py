# Creating a class
class Train:
    def __init__(self, name, fare, seats):  # Defining a constructor with different arguments
        self.name = name  # Defining class attribute
        self.fare = fare  # Defining class attribute
        self.seats = seats  # Defining class attribute
        self.passenger_name = None  # Defining class attribute

    def getInfo(self):  # Defining a function
        print(f"Name of the train is {self.name}")  # Writing methods
        print(f"Fare of this train is {self.fare} rupees only")  # Writing methods
        print(f"Total seats available in this train is {self.seats}")  # Writing methods

    def getTicket(self):  # Defining a function
        if self.seats > 0:  # Writing methods from line number(15-19)
            print(f"{self.passenger_name} your ticket is booked and your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry! no seat available in this train")


Rajdhani = Train("Patna-Delhi Rajdhani 24057", 3500, 300)  # Instantiating an object
Intercity = Train("Patna-Saharsa Intercity 21095", 70, 530)  # Instantiating an object
Garibrath = Train("Delhi-Patna Garibrath Express 29058", 1700, 430)  # Instantiating an object

user = input("Enter train name: (RJD) for RAJDHANI, (INTC) for INTERCITY, (GRB) for GARIBRATH > ")

# Creating conditions from line number(29-37)
if user == "RJD":
    Rajdhani.getInfo()
    selected_train = Rajdhani
elif user == "INTC":
    Intercity.getInfo()
    selected_train = Intercity
else:
    Garibrath.getInfo()
    selected_train = Garibrath

selected_train.passenger_name = input("Enter the passenger name: ")  # Taking input from user
n = int(input("Number of seats to book: "))  # Taking input from user

# Creating a while loop
while n > 0:
    selected_train.getTicket()
    n = n - 1

selected_train.getInfo()
