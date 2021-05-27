class Atm(object):
    def __init__(self, cardno, pin):
        self.cardno = cardno
        self.pin = pin
    
    def withdrawal(self):
        print("Withdrawing cash.")
    
    def enquiry(self):
        print("Checking balance.")
    
thing = Atm(69692021, 4201)

thing.withdrawal()
thing.enquiry()