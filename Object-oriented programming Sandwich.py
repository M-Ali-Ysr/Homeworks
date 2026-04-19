class Sandwich:
    def __init__(self,name,materials1,materials2,materials3,materials4,materials5,materials6):
        self._name = name
        self._materials1 = materials1
        self._materials2 = materials2
        self._materials3 = materials3
        self._materials4 = materials4
        self._materials5 = materials5
        self._materials6 = materials6
        self.stock = {self._materials1 : int(input(f"How many of {materials1} are there? ")), self._materials2 : int(input(f"How many of {materials2} are there? ")),
                     self._materials3 : int(input(f"How many of {materials3} are there? ")), self._materials4 : int(input(f"How many of {materials4} are there? "))}
    def info(self):
        print(f"The ingredients that will go into {self._name}'s sandwich:\n1-{self._materials1} \n2-{self._materials2} \n3-{self._materials3} \n4-{self._materials4} \n5-{self._materials5} \n6-{self._materials6}")
    def control(self):
        if self.stock[self._materials1] == 0:
            print(f"We are completely out of stock of {self._materials1}. We're Sorry! Would you like antoher metarial?")
        if self.stock[self._materials2] == 0:
            print(f"We are completely out of stock of {self._materials2}. We're Sorry! Would you like antoher metarial?")
        if self.stock[self._materials3] == 0:
            print(f"We are completely out of stock of {self._materials3}. We're Sorry! Would you like antoher metarial?")
        if self.stock[self._materials4] == 0:
            print(f"We are completely out of stock of {self._materials4}. We're Sorry! Would you like antoher metarial?")
        elif self.stock[self._materials1] > 0 and self.stock[self._materials2] > 0 and self.stock[self._materials3] > 0 and self.stock[self._materials4] > 0:
            print("Your order is being prepared...")
member=Sandwich(f"{input("Please Enter Your Name:\n")}",f"{input("Please Enter The Metarial You Require:\n")}",
                f"{input("Please Enter The Metarial You Require:\n")}",f"{input("Please Enter The Metarial You Require:\n")}",
                f"{input("Please Enter The Metarial You Require:\n")}",f"{input("Please Enter Your Preffered Sauce:\n")}",
                f"{input("Please Enter Your Preffered Sauce:\n")}")
member.info()
member.control()