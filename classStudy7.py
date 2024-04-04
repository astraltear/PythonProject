
import classStudy6

class PohamCar:
    turnShow='stop'

    def __init__(self,ownerName):
        self.ownerName = ownerName
        self.handle = classStudy6.PohamHandle()


    def TurnHandle(self,q):
        if q > 0:
            self.turnShow = self.handle.RightTurn(q)

        elif q < 0 :
            self.turnShow = self.handle.LeftTurn(q)

        else :
            self.turnShow = self.handle.Straight(q)


tom = PohamCar('tom')
tom.TurnHandle(10)
print(tom.ownerName,tom.turnShow, tom.handle.quantity)


james = PohamCar('james')
james.TurnHandle(-20)
print(james.ownerName,james.turnShow, james.handle.quantity)