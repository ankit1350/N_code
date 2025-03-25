from random import randint
class Train:

    def __init__(ankit,trainNo):
        ankit.trainNo=trainNo
    def book(ankit,fro,to):
        print(f"Ticket booked in trainNo.{ankit.trainNo} from {fro}to{to}")
    def status(ankit):
        print(f"trainno.{ankit.trainNo}is running on time")
    def get_fare(ankit,fro,to):
        print(f"the fare for trainno.{ankit.trainNo}from{fro}to {to}is {randint(1000,5000)}")
        

t=Train(23233)
t.book("pune","patna")
t.status()
t.get_fare("pune","patna")