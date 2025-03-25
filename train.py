from random import randint
class Train:

    def __init__(self,trainNo):
        self.trainNo=trainNo
    def book(self,fro,to):
        print(f"Ticket booked in trainNo.{self.trainNo} from {fro}to{to}")
    def status(self):
        print(f"trainno.{self.trainNo}is running on time")
    def get_fare(self,fro,to):
        print(f"the fare for trainno.{self.trainNo}from{fro}to {to}is {randint(1000,5000)}")
        

t=Train(23233)
t.book("pune","patna")
t.status()
t.get_fare("pune","patna")