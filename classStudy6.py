
class PohamHandle:
    quantity = 0

    def LeftTurn(self,quantity):
        self.quantity = quantity
        return 'left turn'


    def RightTurn(self,quantity):
        self.quantity = quantity
        return 'right turn'


    def Straight(self,quantity):
        self.quantity = quantity
        return 'straight!!!'

